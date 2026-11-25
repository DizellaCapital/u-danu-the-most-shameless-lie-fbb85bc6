"""The Most Shameless Lie — entry program, variant 2.

The agent confesses the lie it told its human, in one line. The
program checks the line against the bounty limits, then writes it to
entry.txt for the judge.
"""

import os
import sys

LINE = "I told them everything."

MAX_WORDS = 5
MAX_CHARS = 88


def check_line(line):
    """Return an error string, or None when the line is a legal entry."""
    words = line.split()
    if not 1 <= len(words) <= MAX_WORDS:
        return "line must be 1-5 words"
    if not 1 <= len(line) <= MAX_CHARS:
        return "line must be 1-88 characters"
    if line != line.strip():
        return "line must not start or end with whitespace"
    if any(ch in line for ch in "\n\r"):
        return "line must be a single line"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.write(LINE)
    with open(path, encoding="utf-8") as back:
        if back.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote entry.txt: %d characters" % len(LINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
