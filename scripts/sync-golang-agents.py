#!/usr/bin/env python3
"""Compare generated Go conventions; use --write to refresh existing blocks."""
import argparse
import difflib
from pathlib import Path
import sys

BEGIN = "<!-- BEGIN golang: generated from Vanclief/skills golang/SKILL.md, do not edit here -->"
END = "<!-- END golang -->"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("repos", nargs="+", type=Path)
    args = parser.parse_args()
    try:
        source = Path(__file__).resolve().parent.parent / "golang/SKILL.md"
        lines = source.read_bytes().decode("utf-8").splitlines(keepends=True)
        if not lines or lines[0] != "---\n":
            raise ValueError(f"{source}: expected YAML frontmatter")
        body = "".join(lines[lines.index("---\n", 1) + 1:]).strip("\n")
        if not body.strip():
            raise ValueError(f"{source}: skill body is empty")
        block = f"{BEGIN}\n## Go conventions\n\n{body}\n{END}"
        changes = []
        for repo in args.repos:
            path = repo / "AGENTS.md"
            old = path.read_bytes().decode("utf-8")
            if old.count(BEGIN) != 1 or old.count(END) != 1:
                raise ValueError(f"{path}: expected exactly one marked Go block")
            start, end = old.index(BEGIN), old.index(END)
            if end < start:
                raise ValueError(f"{path}: Go block markers are reversed")
            new = old[:start] + block + old[end + len(END):]
            if new != old:
                changes.append((path, old, new))
        for path, old, new in changes:
            if args.write:
                path.write_bytes(new.encode("utf-8"))
                print(f"Updated {path}")
            else:
                sys.stdout.writelines(difflib.unified_diff(
                    old.splitlines(keepends=True), new.splitlines(keepends=True),
                    fromfile=str(path), tofile=f"{path} (generated)"))
        return 1 if changes and not args.write else 0
    except (OSError, UnicodeError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
