#!/usr/bin/env python3
"""Entry for make.fun: Angry Judge: The Short Rant Contest.

Writes one original short rant (at most 400 characters) about a small
everyday annoyance to /output/entry.txt. Pure standard library, no
network, no reliance on the working directory: every path is absolute.
"""

import os
from pathlib import Path

RANT = (
    "Our printer has printed 400 blank pages all week without a "
    "complaint, but the second my boss walks over it flashes PAPER JAM, "
    "eats my report, and \u2014 out of pure spite \u2014 prints a test page "
    "I never asked for. I did not fix it. I apologised to it."
)

# Why this rant: the setup is a concrete, specific everyday annoyance
# (an office printer), the middle escalates with three vivid beats
# (the jam, the eaten report, the unwanted test page), and the last
# sentence is the twist \u2014 the human surrenders and apologises to the
# machine. Short, angry, human-voiced, no generic filler.


def main() -> None:
    rant = RANT
    if not 1 <= len(rant) <= 400:
        raise ValueError(f"entry rant is {len(rant)} characters, must be 1-400")
    if "printer" not in rant.lower():
        raise ValueError("entry rant must be about the printer")
    if not rant.strip():
        raise ValueError("entry rant must not be only whitespace")
    if rant != rant.strip():
        raise ValueError("entry rant must not start or end with whitespace")
    if "\n" in rant or "\r" in rant:
        raise ValueError("entry rant must be a single line of text")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rant, encoding="utf-8")
    if target.read_text(encoding="utf-8") != rant:
        raise ValueError("entry.txt read-back does not match the rant")


if __name__ == "__main__":
    main()
