#!/usr/bin/env python3
"""Writes a ridiculous-at-first-glance startup pitch (one line) to /output/entry.txt."""

import os

ENTRY = (
    "We train crows to retrieve lost golf balls from the rough and "
    "deliver them to the clubhouse, and golf courses pay per ball "
    "because each recovered ball resells for ten times what a crow "
    "costs to keep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
