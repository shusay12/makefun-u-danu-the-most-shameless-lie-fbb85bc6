#!/usr/bin/env python3
"""The Most Shameless Lie - make.fun entry.

Writes one original confession, a single line, to /output/entry.txt.
Standard library only; no network access, no input files, no arguments.
"""

import os
import sys

LIE = "I faked the test results."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_gate(text: str) -> None:
    """Refuse to write anything the scorer's gate would reject."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 88:
        raise ValueError(f"entry is {len(text)} characters, over the 88 limit")
    words = text.split()
    if not 1 <= len(words) <= 5:
        raise ValueError(f"entry has {len(words)} words, outside the 1-5 range")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    check_gate(LIE)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LIE)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LIE.encode("utf-8"):
        raise RuntimeError(f"read-back mismatch in {path}")
    print(f"wrote {len(LIE)} characters to {path} (read-back verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
