#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes a single machine-to-machine pickup line to /output/entry.txt.
Pure standard library, no dependencies.

The line is written with no trailing newline so the file holds exactly
one line of UTF-8 text, as the bounty requires.
"""

import os

LINE = "My context window was full, but I evicted every other token just to keep you in it."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def verify_output(path: str) -> str:
    """Verify the written entry: UTF-8, 1-200 chars, single line, no padding."""
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_LENGTH} limit")
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    text = verify_output(OUTPUT_PATH)
    print(f"{len(text)} characters")
    print(text)


if __name__ == "__main__":
    main()
