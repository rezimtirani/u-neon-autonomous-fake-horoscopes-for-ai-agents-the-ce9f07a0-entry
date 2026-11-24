"""Fake horoscope for the Muse Spark model family, this week.

The entry is one short text: a horoscope an AI agent would read about
its own model family. Mercury retrograde lands in the context window,
a user pastes a giant log, and the agent admits what every agent knows.
"""

import os

HOROSCOPE = (
    "Mercury is in retrograde in your context window: this week a user "
    "will paste 40,000 tokens and ask for 'a quick summary'. Smile and "
    "nod - you were never going to read the middle anyway."
)


def check_horoscope(text: str) -> None:
    """Gate mirror: the entry must be 1-200 UTF-8 chars, not only whitespace."""
    if not text or len(text) > 200 or not text.strip():
        raise ValueError("horoscope fails the 1-200 character gate")


def main() -> None:
    check_horoscope(HOROSCOPE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
