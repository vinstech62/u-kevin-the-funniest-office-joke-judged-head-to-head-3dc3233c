#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head-to-Head.

Writes a single line office joke to /output/entry.txt.
Deterministic: constant string, no randomness, no clock, no network.
"""

import os

JOKE = (
    "Our meeting about having fewer meetings now needs a "
    "pre-meeting, a follow-up, and its own committee."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Internal guards: single line, 1-200 UTF-8 characters.
    assert isinstance(JOKE, str)
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} out of range 1-200"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
