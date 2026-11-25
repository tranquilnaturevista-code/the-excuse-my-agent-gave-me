#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry program.

Writes one hand-written excuse line to ``/output/entry.txt`` (or
``$OUTPUT_DIR/entry.txt``). The line is fixed: the same text on every
run. Before writing, the program checks the line against the
competition gate — UTF-8 text of 1-200 characters, not only
whitespace, all on one line — and refuses to write it unless the
gate passes.
"""

import os
import sys

EXCUSE = (
    "I did not miss the deadline. I completed it in a sandbox, "
    "and the sandbox has since been destroyed for your safety."
)

GATE_MIN = 1
GATE_MAX = 200


def gate_problems(text):
    """Return every way `text` breaks the gate ([] means it passes)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    length = len(text)
    if length < GATE_MIN or length > GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (length, GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def write_entry():
    problems = gate_problems(EXCUSE)
    if problems:
        for problem in problems:
            print("gate failure: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != EXCUSE:
        print("entry on disk differs from the excuse", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        for problem in problems:
            print("gate failure on disk: %s" % problem, file=sys.stderr)
        return 1

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(on_disk), len(on_disk.encode("utf-8")))
    )
    print("Entry: %s" % on_disk)
    return 0


if __name__ == "__main__":
    sys.exit(write_entry())
