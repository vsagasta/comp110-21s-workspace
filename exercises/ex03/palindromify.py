"""EX03 - palindromify function."""

__author__: str = "730396600"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("live on time ", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("race", False))


def palindromify(string: str, type: bool) -> str:
    """A function that turns a string into a palindrome."""
    if type:
        item: str = string
        i = len(string) - 1
        while i >= 0:
            item += string[i]
            i -= 1
        return(item)
    else:
        item = string
        i = len(string) - 2
        while i >= 0:
            item += string[i]
            i -= 1
        return(item)


if __name__ == "__main__":
    main()