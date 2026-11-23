#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. Standard library only; no network access.
"""

import os

LINE = (
    "CAUTION: Will keep pressing 'Remind me later' until the deadline "
    "it was reminding them about has already passed."
)


def validate(line: str) -> None:
    """Mirror the sealed gate: 1-160 UTF-8 chars, one non-blank line."""
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry is {len(line)} characters, must be 1-160")
    line.encode("utf-8")  # must round-trip as UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Verify the written file round-trips exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8").rstrip("\n")
    if written != LINE:
        raise ValueError("written entry does not match the line")
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
