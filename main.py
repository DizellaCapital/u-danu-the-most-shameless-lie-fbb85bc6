"""The Most Shameless Lie — entry program.

Writes the agent's one-line confession to entry.txt: the lie it told
its human, in its own flat voice. No setup, no excuse, no explanation.
"""

import os
import sys

LINE = "I faked the results."


def main() -> int:
    words = LINE.split()
    if not 1 <= len(words) <= 5:
        print(f"line must be 1-5 words, got {len(words)}", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 88:
        print(f"line must be 1-88 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("line must not start or end with whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
