#!/usr/bin/env python3
"""Writes one satirical sentence to /output/entry.txt.

Entry for make.fun competition
u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
(The Long Roast: Lawmakers and the File They Cannot Convert).
"""

import os

SENTENCE = (
    "They want a kill switch for AI, a registry for crypto, and a leash "
    "on the internet \u2014 all drafted in a Word doc nobody in the building "
    "can turn into a PDF."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
