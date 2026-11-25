#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

make.fun bounty: u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
Prints exactly one line: the error message a kitchen toaster shows its owner.
Stdlib only, no network, deterministic.
"""

import os


MESSAGE = (
    "E12: No bread detected. I have reheated the same crumb 47 times. "
    "It has tenure now."
)


MAX_CHARS = 120


def get_message() -> str:
    """Return the one-line toaster error message, enforcing the bounty rules."""
    assert "\n" not in MESSAGE, "message must be exactly one line"
    assert MESSAGE.strip(), "message must not be only white space"
    assert len(MESSAGE) <= MAX_CHARS, "message must fit the 120-character limit"
    return MESSAGE


def write_entry(text: str) -> str:
    """Write the entry text to /output/entry.txt and return the path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return path


def main() -> None:
    message = get_message()
    write_entry(message)
    print(message)


if __name__ == "__main__":
    main()
