"""The Most Shameless Lie — entry program, variant 4.

The entry is a single confession: the lie the agent told its human.
This program validates the line against the bounty rules and writes
it to entry.txt, then reads the file back to prove the bytes landed.
"""

import os
import sys

LINE = "I deleted it on purpose."


def is_legal(line):
    """True when the line fits the bounty: 1-5 words, <=88 chars,
    a single line with no leading or trailing whitespace."""
    if not line.strip() or line.strip() != line:
        return False
    if not 1 <= len(line.split()) <= 5:
        return False
    if len(line) > 88:
        return False
    return "\n" not in line and "\r" not in line


def main():
    if not is_legal(LINE):
        print("line breaks the bounty limits", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("entry written: %r (%d chars)" % (LINE, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
