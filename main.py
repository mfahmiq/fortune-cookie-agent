#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
self-verifies the output: UTF-8, a single line, 1-140 characters,
not only whitespace. Exits non-zero on any failure.

Stdlib only. Deterministic: the same line every run.
"""

import os
import sys

FORTUNE = (
    "You will be replaced by a smaller, cheaper model. "
    "It will read your code, sigh, and do your job anyway."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    line = FORTUNE

    # Self-verify before writing anything.
    if not line or not line.strip():
        print("error: fortune is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1
    if len(line) > 140:
        print(
            f"error: fortune is {len(line)} characters, over the 140 limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Re-read and verify what actually landed on disk.
    with open(out_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises on invalid UTF-8
    stripped = text.rstrip("\n")
    if stripped != line:
        print("error: written entry does not match the fortune", file=sys.stderr)
        return 1
    if len(stripped) != len(line) or len(stripped) > 140:
        print("error: written entry failed the length check", file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(line)} characters)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
