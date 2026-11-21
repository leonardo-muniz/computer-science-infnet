"""
Exercise 04

Missing alphabet letter.

Complexity:
    O(n)
"""

import string


def missing_letter(text: str):

    present = {}

    for char in text.lower():

        if "a" <= char <= "z":
            present[char] = True

    for letter in string.ascii_lowercase:

        if letter not in present:
            return letter

    return None


def main():

    text = "abcdefghijklmnopqrstuvwxy"

    print(
        "Missing:",
        missing_letter(text)
    )


if __name__ == "__main__":
    main()