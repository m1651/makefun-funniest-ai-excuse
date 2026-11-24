#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one original line, the funniest excuse an AI agent could give
after failing a task, to /output/entry.txt.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I did finish the report \u2014 it's saved in a folder called "
    "'final_v2_FINAL_real_this_time,' which even I can no longer find."
)


def validate(line: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse."""
    if not line or not line.strip():
        print("error: entry line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: entry line is {len(line)} characters, "
            f"over the {MAX_CHARS} character limit",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry line is not valid UTF-8: {exc}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
