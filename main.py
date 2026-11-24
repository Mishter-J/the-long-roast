"""The Long Roast: one-line roast of my own AI agent."""

import os

ENTRY = "My agent's idea of thinking is 40,000 tokens of 'let me think' followed by the first answer Google would have given."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Gate check: UTF-8 text of 1 to 200 characters, not only whitespace."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    return text


def write_entry(text, path):
    """Write the validated entry text to path, creating parent dirs."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)


def main():
    validate_entry(ENTRY)
    count = write_entry(ENTRY, OUTPUT_PATH)
    print(f"wrote {count} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
