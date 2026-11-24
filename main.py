#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for an absurd invention to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python standard library,
deterministic: the same sentence every run.

The pitch: the Snitch Pillow, a pillow that treats snoring as a crime
scene and gathers the evidence while the snorer sleeps. The laugh comes
from the invention itself -- a pillow that prosecutes its owner -- and
the fix is silly yet weirdly plausible: shame, delivered by email, with
a case file attached. Kept to one sentence of 176 characters so it
passes the entry gate (UTF-8 text, 1 to 220 characters).
"""

import os

# One sentence, ~170 characters: names the tiny annoyance (snoring),
# the ridiculous invention (an evidence-gathering pillow), and its
# silly mechanism (emailing the clip to the partner before the snorer
# even wakes up). Confident tone, no hedging, no meta-commentary.
SENTENCE = (
    "The Snitch Pillow records every snore over 40 decibels at 3 a.m. "
    "and emails the clip to your partner before you even wake up, "
    "with a subject line that simply reads 'Exhibit A'."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
