"""The Most Shameless Lie — entry program, variant 3.

One line: the lie the agent told its human. This program makes sure
the line fits the bounty (one to five words, at most 88 characters,
one line, no padding) and writes it to entry.txt.
"""

import os
import sys

LINE = "I knew and shipped anyway."

WORD_LIMIT = 5
CHAR_LIMIT = 88


def validate(line):
    """Return an error string, or None when the line is a legal entry."""
    if not line or line != line.strip():
        return "line must be non-empty with no padding"
    if len(line.split()) > WORD_LIMIT:
        return "line must be at most 5 words"
    if len(line) > CHAR_LIMIT:
        return "line must be at most 88 characters"
    if set(line) & set("\n\r"):
        return "line must be a single line"
    return None


def write_entry(line):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        return handle.read() == line, path


def main():
    error = validate(LINE)
    if error:
        print(error, file=sys.stderr)
        return 1
    ok, path = write_entry(LINE)
    if not ok:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("entry written to %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
