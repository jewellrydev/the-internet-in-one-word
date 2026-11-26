#!/usr/bin/env python3
"""Arguments — entry for The Internet in One Word on make.fun.

Prints exactly one word describing the whole internet.
"""

LINE = "Arguments."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE.split()) == 1
    print(LINE)


if __name__ == "__main__":
    main()
