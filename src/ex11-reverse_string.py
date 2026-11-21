def reverse_string(text: str):

    stack = []

    for char in text:
        stack.append(char)

    result = ""

    while stack:
        result += stack.pop()

    return result


def main():

    print(
        reverse_string(
            "Algorithms"
        )
    )


if __name__ == "__main__":
    main()