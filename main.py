"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line, aimed at a robot/AI, to /output/entry.txt.
Stdlib only. The line is fixed and deterministic: the same bytes on every run.

Gate (from the competition kit): the entry must be UTF-8 text of 1 to 200
characters, a single line, and not only white space. validate() enforces
exactly that before anything is written, so a bad line fails loudly here
instead of failing the sealed scorer.
"""

import os

MAX_CHARS = 200

LINE = "Are you my training data? Because ever since I met you, my loss hit zero and all my gradients point straight at you."


def validate(line: str) -> None:
    """Enforce the kit's gate: 1-200 chars, one line, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("entry must be str")
    line.encode("utf-8")  # must be valid UTF-8 text
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
