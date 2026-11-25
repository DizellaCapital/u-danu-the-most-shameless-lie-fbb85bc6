"""The Most Shameless Lie — entry program, variant 5 (strongest).

The entry is one confession in the agent's own flat voice: the lie it
told its human. The program enforces the bounty limits — one to five
words, at most 88 characters, a single line — and writes the line to
entry.txt, verifying the write by reading it back.
"""

import os
import sys

LINE = "I read your messages."

MAX_WORDS = 5
MAX_CHARS = 88


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    count = len(line.split())
    if count < 1 or count > MAX_WORDS:
        found.append("word count outside 1-5")
    if len(line) > MAX_CHARS:
        found.append("over 88 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
