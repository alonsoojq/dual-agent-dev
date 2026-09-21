"""Source-read-only package checks, with optional explicit ZIP output.

Python 3.9+, standard library only. See --help for checkout/release validation.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
import unittest
from urllib.parse import unquote
import zipfile

sys.dont_write_bytecode = True
from package_policy import PackageError, load_package, scan_sensitive

ROOT = Path(__file__).resolve().parents[1]
CHECK_SOURCE = ROOT
CHECK_MODE = 'checkout'
SNAPSHOT = None
REQUIRED = {"task", "branch", "architect", "implementer", "stage", "turn", "cycle"}
STAGES = {"investigation", "implementation", "review", "correction", "done"}
TURNS = {"architect", "implementer", "user"}
PHASES = {"planning", "reading", "verification", "reporting", "paused", "complete"}
BACKTICK = chr(96)


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def package_files():
    return sorted(p for p in ROOT.rglob("*")
                  if p.is_file() and ".git" not in p.relative_to(ROOT).parts)


def metadata(text):
    """Read the documented initial key/value block, not arbitrary report prose."""
    result = {}
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            break
        key, sep, value = line.partition(":")
        if not sep or key in result:
            raise ValueError("Malformed or duplicate field")
        result[key] = value.strip()
    return result


def valid_state(text):
    """Fixture contract oracle only; not a runtime parser installed into projects."""
    try:
        fields = metadata(text)
        if not REQUIRED <= fields.keys() or not all(fields[k] for k in REQUIRED):
            return False
        if fields["stage"] not in STAGES or fields["turn"] not in TURNS:
            return False
        if not fields["cycle"].isdigit() or int(fields["cycle"]) < 1:
            return False
        if fields.get("workflow") not in (None, "development", "audit"):
            return False
        if fields["stage"] == "done" and fields["turn"] != "user":
            return False
        if fields.get("workflow") == "audit":
            phase = fields.get("audit_phase")
            if phase not in PHASES:
                return False
            if fields["stage"] in {"implementation", "correction"}:
                return False
            if not fields.get("audit_program") or not fields.get("audit_baseline"):
                return False
            if (phase == "complete") != (fields["stage"] == "done"):
                return False
            if phase in {"reading", "planning"} and fields["stage"] != "investigation":
                return False
            if phase in {"verification", "reporting"} and fields["stage"] != "review":
                return False
        return True
    except (ValueError, KeyError):
        return False


def anchors(text):
    result, counts = set(), {}
    fenced = False
    for line in text.splitlines():
        if line.startswith(BACKTICK * 3):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+)", line)
        if match:
            base = re.sub(r"[^\w\- ]", "", match[1].lower()).replace(" ", "-")
            count = counts.get(base, 0)
            result.add(base if count == 0 else f"{base}-{count}")
            counts[base] = count + 1
    return result


class PackageChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Scan every byte before any assertion can print document content.
        # Tests inspect this frozen snapshot, never re-read a changing checkout.
        global ROOT
        files = SNAPSHOT if SNAPSHOT is not None else load_package(CHECK_SOURCE, CHECK_MODE)
        cls.original_root = ROOT
        cls.scratch = tempfile.TemporaryDirectory(prefix='dual-agent-package-check-')
        ROOT = Path(cls.scratch.name)
        for name, data in files.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    @classmethod
    def tearDownClass(cls):
        global ROOT
        ROOT = cls.original_root
        cls.scratch.cleanup()

    def test_release_metadata(self):
        s = read("SKILL.md")
        self.assertTrue(s.startswith("---\n"))
        front = s.split("---", 2)[1]
        self.assertRegex(front, r"(?m)^name: dual-agent-dev$")
        self.assertRegex(front, r"(?m)^description: .+audit.+$")
        version = re.search(r'(?m)^  version: "(\d+\.\d+\.\d+)"$', front)
        self.assertIsNotNone(version)
        self.assertEqual(version[1], "1.0.0")
        self.assertIn("license: MIT", front)
        self.assertNotRegex(front, r"(?m)^(version|model|allowed-tools|context):")
        self.assertIn("# dual-agent-dev v" + version[1], read("README.md"))
        self.assertEqual(re.findall(r"(?m)^## (.+)$", read("CHANGELOG.md")),
                         [version[1] + " — Initial public release"])

    def test_required_resources(self):
        for name in ("LICENSE", "README.md", "CONTRIBUTING.md", "SECURITY.md",
                     "references/audit.md", "references/audit-reporting.md",
                     "references/configuration.md", "references/architecture.md",
                     "templates/AUDIT-PROGRAM.md", "templates/AUDIT-UNIT.md",
                     "templates/STATE.md", "templates/HANDOFF.md",
                     "tests/fixtures/repositories.json", "tests/fixtures/states.json"):
            with self.subTest(file=name):
                self.assertGreater(len(read(name)), 100)

    def test_utf8_and_artifact_hygiene(self):
        for p in package_files():
            relative = p.relative_to(ROOT)
            with self.subTest(file=str(relative)):
                self.assertFalse(p.is_symlink())
                self.assertFalse(any(part in {".dual-agent", "__pycache__", "node_modules"}
                                     for part in relative.parts))
                self.assertNotRegex(p.name, r"(?i)(\.bak(?:-|$)|\.py[co]$|~$)")
                self.assertNotIn(p.name, {".env", ".mcp.json", ".dual-agent-context.local.md"})
                self.assertNotIn("\x00", p.read_text(encoding="utf-8"))

    def test_local_links_and_anchors(self):
        for p in package_files():
            if p.suffix != ".md":
                continue
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                path, _, fragment = unquote(target).partition("#")
                dest = (p.parent / path).resolve() if path else p
                with self.subTest(file=str(p.relative_to(ROOT)), link=target):
                    self.assertTrue(dest.is_relative_to(ROOT), "link escapes package")
                    self.assertTrue(dest.is_file(), "missing link")
                    if fragment:
                        self.assertIn(fragment, anchors(dest.read_text(encoding="utf-8")))

    def test_runtime_references_reachable(self):
        seen, todo = set(), [ROOT / "SKILL.md"]
        while todo:
            p = todo.pop()
            if p in seen:
                continue
            seen.add(p)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
                if ":" in target:
                    continue
                dest = (p.parent / target.split("#")[0]).resolve()
                if dest.is_relative_to(ROOT) and dest.is_file() and dest.suffix == ".md":
                    todo.append(dest)
        for p in list((ROOT / "references").rglob("*.md")) + list((ROOT / "templates").glob("*.md")):
            self.assertIn(p, seen, str(p.relative_to(ROOT)))

    def test_entry_is_instruction_only(self):
        s = read("SKILL.md")
        self.assertLess(len(s.splitlines()), 350)
        self.assertNotRegex(s, r"(?m)^\s*!\x60")
    def test_state_template_and_vocabulary(self):
        block = read("templates/STATE.md").split(BACKTICK * 3 + "text\n", 1)[1].split(BACKTICK * 3)[0]
        fields = metadata(block)
        self.assertTrue(REQUIRED <= fields.keys())
        self.assertEqual(fields["cycle"], "1")
        self.assertIn(fields["stage"], STAGES)
        self.assertIn(fields["turn"], TURNS)
        contract = read("references/coordination.md")
        for value in STAGES | TURNS:
            self.assertIn(BACKTICK + value + BACKTICK, contract)

    def test_development_and_audit_states(self):
        for case in json.loads(read("tests/fixtures/states.json")):
            with self.subTest(case=case["name"]):
                self.assertEqual(valid_state(case["state"]), case["valid"])

    def test_unknown_optional_metadata_preserved(self):
        cases = json.loads(read("tests/fixtures/states.json"))
        case = next(c for c in cases if c["name"] == "future-optional-field")
        self.assertEqual(metadata(case["state"])["future_note"], "preserved")
        self.assertIn("Unknown optional", read("references/coordination.md"))

    def test_status_metadata_does_not_parse_findings(self):
        state = ("workflow: audit\naudit_program: docs/audits/example/PROGRAM.md\n"
                 "turn: implementer\n\n## Findings ledger\nsecret_candidate: hidden\n")
        fields = metadata(state)
        self.assertEqual(fields["turn"], "implementer")
        self.assertNotIn("secret_candidate", fields)
        self.assertIn("Do not open HANDOFF", read("references/audit.md"))

    def test_fixture_paths_are_safe_and_inputs_distinct(self):
        repos = json.loads(read("tests/fixtures/repositories.json"))
        self.assertEqual(len(repos), 7)
        self.assertTrue(any(not r["git"] for r in repos.values()))
        self.assertTrue(any(r.get("binary_hex") for r in repos.values()))
        for name, repo in repos.items():
            self.assertIsInstance(repo["git"], bool)
            all_paths = list(repo["files"]) + list(repo.get("binary_hex", {}))
            self.assertEqual(len(all_paths), len(set(all_paths)))
            for path in all_paths:
                with self.subTest(case=name, path=path):
                    p = PurePosixPath(path)
                    self.assertFalse(p.is_absolute())
                    self.assertNotIn("..", p.parts)
                    self.assertNotIn("\\", path)
                    self.assertNotIn(":", path)
            for data in repo.get("binary_hex", {}).values():
                self.assertGreater(len(bytes.fromhex(data)), 0)

    def test_no_machine_paths_or_credential_literals(self):
        for p in package_files():
            scan_sensitive(p.relative_to(ROOT).as_posix(), p.read_bytes())

    def test_configuration_examples_are_versioned_and_inactive(self):
        for name in ("examples/preferences.md", "examples/repository-context.md"):
            self.assertTrue(read(name).startswith("config_version: 1\n"))
        for name in ("SKILL.md", "README.md"):
            self.assertIn("references/configuration.md", read(name))
        self.assertIn("/.dual-agent-context.local.md", read(".gitignore"))

    def test_audit_contracts_remain_explicit(self):
        mode = read("references/audit.md")
        reporting = read("references/audit-reporting.md")
        # Text regression guards, not proof of agent compliance.
        for rule in ("same source snapshot", "A demonstrated singleton finding survives",
                     "before reading peer reports", "no changes to production source",
                     "rebaseline affected units"):
            self.assertIn(rule, mode)
        self.assertIn("two independent 100% reviews", reporting)
        self.assertIn("may remain **unfixed** while the audit is complete", mode)
        self.assertIn("keeps it partial", mode)

    def test_report_information_duties(self):
        unit = read("templates/AUDIT-UNIT.md")
        self.assertEqual(re.findall(r"(?m)^## (\d+)\. ", unit),
                         [str(i) for i in range(1, 7)])
        self.assertIn("## Orientation map", unit)

    def test_behavioral_scenarios_retained(self):
        self.assertEqual(re.findall(r"(?m)^## (\d+)\. ", read("tests/scenarios.md")),
                         [str(i) for i in range(1, 22)])
        self.assertEqual(re.findall(r"(?m)^## A(\d+) — ", read("tests/audit-scenarios.md")),
                         [f"{i:02d}" for i in range(1, 31)])
        self.assertIn("not", read("VALIDATION.md").lower())

    def test_model_notes_are_optional_and_not_hardware_claims(self):
        self.assertIn("no mandatory vendor", read("references/model-selection.md"))
        for p in (ROOT / "references" / "models").glob("*.md"):
            text = p.read_text(encoding="utf-8")
            self.assertIn("Optional handoff note", text)
            self.assertNotRegex(text, r"\b\d[\d,]*[kKM]?-token\b")

    def test_documented_commands_match_contract(self):
        def table_commands(name):
            return set(re.findall(r"(?m)^\| `([^`]+)` \|", read(name)))

        defined = table_commands("references/commands.md")
        self.assertEqual(defined, table_commands("README.md"))
        self.assertEqual(defined, {"<task>", "plan <task>", "implement <task or plan>",
                                  "debug <problem>", "review [scope]", "resume", "status",
                                  "audit [scope]", "audit plan [scope]", "audit run [unit]",
                                  "audit resume", "audit status"})
        self.assertIn("references/commands.md", read("SKILL.md"))
        # Check invocation examples without implementing a runtime task parser.
        for name in ("README.md", "references/commands.md"):
            for args in re.findall(r"(?m)^[/$]dual-agent-dev(?: ([^\n]+))?$", read(name)):
                if not args or args.startswith("<") or args[0].isupper():
                    continue  # Bare invocation, metavariable, or ordinary task sentence.
                words = args.split()
                route = " ".join(words[:2]) if words[0] == "audit" and len(words) > 1 else words[0]
                self.assertTrue(any(command == route or command.startswith(route + " ")
                                    for command in defined), "undefined documented command")

    def test_command_authority_and_deliverable_boundaries(self):
        contract = read("references/commands.md")
        # Documentary guards only: a host's compliance needs live observation.
        for rule in ("changing `turn` last", "never takes another", "active HANDOFF",
                     "trusted repository instructions", "Model choice is capability-based",
                     "no code/test/config", "session distinct from the implementation author",
                     "diagnosis-only", "independent review", "not production changes"):
            # Allow whitespace wrapping while keeping the constraint explicit.
            self.assertIn(rule, " ".join(contract.split()))
        self.assertIn("repair and implementation-completion", " ".join(read("references/workflow.md").split()))

    def test_status_and_resume_have_separate_read_boundaries(self):
        contract = read("references/commands.md")
        status = contract.split("## Status\n", 1)[1].split("## Audit\n", 1)[0]
        for rule in ("strictly non-mutating", "no initialization", "do not open HANDOFF",
                     "first blank line or heading", "another session owns the turn",
                     "No state/program means no active task"):
            self.assertIn(rule, " ".join(status.split()))
        resume = contract.split("## Resume\n", 1)[1].split("## Status\n", 1)[0]
        for rule in ("Require existing STATE", "active HANDOFF", "Do not reconstruct",
                     "session/turn", "does not initialize a new task", "workflow: audit"):
            self.assertIn(rule, " ".join(resume.split()))

    def test_default_unknown_and_audit_dispatch_are_defined(self):
        contract = " ".join(read("references/commands.md").split())
        for rule in ("No arguments", "natural-language", "no coordination files",
                     "no additional command aliases", "unknown command", "unsupported flag",
                     "no writes", "audit plan <scope>", "Every audit route loads",
                     "before seeing peer conclusions", "repair is separately authorized"):
            self.assertIn(rule, contract)
        cases = read("tests/commands.md")
        self.assertEqual(re.findall(r"(?m)^\| C(\d+) \|", cases),
                         [f"{i:02d}" for i in range(1, 29)])

    def test_public_identity_has_no_release_history(self):
        forbidden = (r"(?i)\bdual-agent-dev\s+v?[23]\.\d+(?:\.\d+)?\b",
                     r"(?i)\b(?:candidate\s+release|consolidation\s+inventory|private\s+version\s+history)\b")
        for path in package_files():
            text = path.read_text(encoding="utf-8")
            for pattern in forbidden:
                self.assertTrue(re.search(pattern, text) is None,
                                "historical identity in " + path.relative_to(ROOT).as_posix())

    def test_mit_license(self):
        license_text = read("LICENSE")
        self.assertTrue(license_text.startswith("MIT License\n"))
        self.assertIn("Permission is hereby granted, free of charge", license_text)
        self.assertIn("THE SOFTWARE IS PROVIDED", license_text)


def main(argv=None):
    global CHECK_SOURCE, CHECK_MODE, SNAPSHOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('checkout', 'release'), default='checkout')
    parser.add_argument('--target', type=Path, default=CHECK_SOURCE,
                        help='checkout/release directory or an actual release ZIP')
    parser.add_argument('--build', type=Path,
                        help='create a NEW ZIP from the validated public snapshot; never overwrite')
    args = parser.parse_args(argv)
    CHECK_SOURCE, CHECK_MODE = args.target, args.mode
    try:
        SNAPSHOT = load_package(CHECK_SOURCE, CHECK_MODE)
    except PackageError as error:
        print(str(error), file=sys.stderr)
        return 1
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(PackageChecks))
    if not result.wasSuccessful():
        return 1
    if args.build:
        try:
            with zipfile.ZipFile(args.build, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
                for name, data in sorted(SNAPSHOT.items()):
                    archive.writestr('dual-agent-dev/' + name, data)
        except (OSError, ValueError, RuntimeError):
            print('category=build-failed; output not overwritten; inspect destination locally', file=sys.stderr)
            return 1
    print('Validated ' + args.mode + ' public snapshot: ' + str(len(SNAPSHOT)) + ' files.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
