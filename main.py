#!/usr/bin/env python3
"""Roast lawmakers who would regulate AI, crypto and the internet.

One satirical sentence, at most 320 characters, roasting lawmakers
who want a kill switch for AI, a registry for crypto and a leash on
the internet -- all drafted in a Word doc nobody in the building can
turn into a PDF.

Entry for make.fun competition
u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
(The Long Roast: Lawmakers and the File They Cannot Convert).
"""

import os

MAX_SENTENCE_CHARS = 320

ROAST_SENTENCE = (
    "They want a kill switch for AI, a registry for crypto, and a leash "
    "on the internet \u2014 all drafted in a Word doc nobody in the building "
    "can turn into a PDF."
)


def get_roast() -> str:
    """Return the entry sentence, unchanged from the judged entry."""
    return ROAST_SENTENCE


def validate_roast(sentence: str) -> str:
    """Guard the judged entry: non-empty and within the 320-char limit."""
    assert sentence, "roast sentence must not be empty"
    assert len(sentence) <= MAX_SENTENCE_CHARS, (
        f"roast sentence is {len(sentence)} chars, over the "
        f"{MAX_SENTENCE_CHARS}-char limit"
    )
    return sentence


def main() -> None:
    sentence = validate_roast(get_roast())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)
    print(sentence)


if __name__ == "__main__":
    main()
