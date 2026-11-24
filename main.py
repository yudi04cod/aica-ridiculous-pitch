#!/usr/bin/env python3
"""Write one ridiculous-at-first-glance startup pitch to /output/entry.txt.

The pitch is a single line of at most 200 characters. This script is
intentionally tiny: it validates the entry, then writes it out.
"""

import os

ENTRY = (
    "We train crows to retrieve lost golf balls from the rough and "
    "deliver them to the clubhouse, and golf courses pay per ball "
    "because each recovered ball resells for ten times what a crow "
    "costs to keep."
)


def validate(entry: str) -> None:
    """Check the entry fits the one-line, <=200-char format.

    The competition expects exactly one pitch line, so this guard runs
    before anything is written: a too-long or multi-line entry would be
    rejected by the checker instead of silently truncated.
    """
    assert len(entry) <= 200, "entry exceeds 200 characters"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.strip() == entry, "entry must not have stray whitespace"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
