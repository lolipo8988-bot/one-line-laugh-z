"""Write one funny line to /output/entry.txt.

One sentence, 103 characters: a cat owner buys a treadmill so the
cat will exercise, and the turn lands in the last few words -- the
cat does use the machine, just for naps, struck in a more athletic
position. Plain, concrete words; nothing explains the joke, and
every word earns its place.

The program is deterministic: every run writes exactly the
same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

TEXT = "I bought my cat a treadmill so she'd exercise, and now she just naps on it in a more athletic position."


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
