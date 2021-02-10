"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730396600"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Given a number, return a fortune."""
    random_value: int = randint(0, 5)
    if random_value == 0:
        return "A dubious friend may be an enemy in camouflage."
    else:
        if random_value == 1:
            return "A feather in the hand is better than a bird in the air."
        else:
            if random_value == 2:
                return "All your hard work will soon pay off."
            else:
                if random_value == 3:
                    return "A short pencil is usually better than a long memory any day."
                else:
                    return "Do not make extra work for yourself."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()