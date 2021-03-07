"""EX03 - avoid_fifth function."""

__author__: str = "730396600"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello there!"))
    print(avoid_fifth("General Kenobi..."))


def avoid_fifth(sentence: str) -> str:
    """A function that removes any E's from a sentence."""
    item: str = ""
    for character in sentence:
        if character != "e" and character != "E":
            item += character
        elif character == "e" or character == "E":
            item += ""
    return(item)


if __name__ == "__main__":
    main()