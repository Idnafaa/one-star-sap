#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing the human who owns it, to /output/entry.txt.

The review: the plant was repotted into a mug with no drainage hole,
blamed for the smell of its own stagnant bathwater, and still gets
introduced to guests as "low maintenance". Setup, grievance, twist,
punchline — in one line, under 280 characters.

Python 3.13, standard library only.
SPDX-License-Identifier: MIT
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 279


def build_review() -> str:
    """Assemble the one-line review from its beats."""
    opener = "One star: she repotted me into a mug with no drainage hole,"
    grievance = "then blamed me for the smell"
    twist = "I have been sitting in my own bathwater for a month,"
    punchline = "and she still tells guests I am \u201clow maintenance\u201d."
    return " ".join([opener, grievance + " \u2014", twist, punchline])


def self_check(text: str) -> None:
    """Enforce the bounty gate before writing anything."""
    if not isinstance(text, str):
        raise TypeError("review must be a string")
    if text != text.strip():
        raise ValueError("review must not start or end with whitespace")
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    text.encode("utf-8")


def main() -> int:
    review = build_review()
    self_check(review)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(review)
    # Read the file back and re-run the gate on exactly what is on disk,
    # so a write failure or stray newline can never slip through silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != review:
        raise ValueError("written file does not match the checked review")
    self_check(written)
    print(f"wrote {len(review)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
