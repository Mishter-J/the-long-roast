#!/usr/bin/env python3
"""The Long Roast — one-line roast of my own AI agent.

Writes the roast to /output/entry.txt (program/v1).

The line was chosen from 10 original candidates by local deterministic
scoring (local_score.py, archetype one-liner: 74.0/100) plus in-session
judging against the judge's published brief: it roasts my own agent,
lands a real turn (40,000 tokens of "thinking" theatre vs a Google-grade
answer), avoids the obvious hallucination / over-apologising angles the
brief names, and stays tight at 116 characters.
"""

import os

ROAST = (
    "My agent's idea of thinking is 40,000 tokens of 'let me think' "
    "followed by the first answer Google would have given."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    print(f"wrote {len(ROAST)} chars to {path}")


if __name__ == "__main__":
    main()
