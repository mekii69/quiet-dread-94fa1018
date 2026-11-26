"""Two Days of Quiet Dread: write one code-review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential dread:
green tests and a clean diff today, and code that will quietly outlive
everyone who approved it, starting with the reviewer. It is built from
parts and validated as a single line of 1-140 characters, no trailing
newline, so the sealed gate reads exactly one line of 1-140 characters.
"""

import os

ENTRY_PARTS = [
    "LGTM. Tests are green, the diff is clean,",
    "and this code will quietly outlive",
    "everyone who approved it, starting with me.",
]
ENTRY = " ".join(ENTRY_PARTS)

if not (1 <= len(ENTRY) <= 140 and "\n" not in ENTRY and ENTRY.strip()):
    raise ValueError("entry must be one non-blank line of 1-140 characters")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
