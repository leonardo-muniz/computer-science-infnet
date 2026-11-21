"""
Exercise 05

First non repeated character.

Complexity:
    O(n)
"""

from collections import defaultdict


def first_non_repeated(text: str):

    freq = defaultdict(int)

    for char in text:
        freq[char] += 1

    for char in text:

        if freq[char] == 1:
            return char

    return None


def main():

    print(
        first_non_repeated("swiss")
    )


if __name__ == "__main__":
    main()