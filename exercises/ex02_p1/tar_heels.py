"""Tar Heels exercise redux as a structured program."""

__author__ = "730396600"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(choice: int) -> str:
    """A function that gives different hords depending on divisibility."""
    two_divisibility: int = choice % 2
    seven_divisibility: int = choice % 7
    if two_divisibility == 0 and seven_divisibility == 0:
        return("TAR HEELS")
    else:
        if two_divisibility == 0 and seven_divisibility != 0:
            return("TAR")
        else:
            if two_divisibility != 0 and seven_divisibility == 0:
                return("HEELS")               
            else:
                return("CAROLINA")


if __name__ == "__main__":
    main()