"""An 8 ball game to provide you the answer to life's most ardent questions."""

from random import randint

def main() -> None:
    """Entrypoint of game."""
    print("Hello! Welcome to the magical 8 ball oracle, a program with the answer to all of life's mysteries.")
    playing: bool = True
    while playing:
        question: str = input("Ask the magic oracle a yes or no question: ")
        random_number: int = randint(0, 10)
        print(answer(random_number))
        playing = input("Continue? yes / no ") == "yes"
    print("Use the infomation bestowed upon you wisely. Good day weary traveler.")


def answer(n: int) -> str:
    """A function that gives you an answer in response to a random integer."""
    if n == 0:
        return "Definitely, yes!"
    elif n == 1:
        return "Better ask again later."
    elif n == 2:
        return "NO. NO. NO!!!"
    elif n == 3:
        return "Unlikely."
    elif n == 4:
        return "Probably."
    elif n == 5:
        return "The answer depends on what you do about it, so take action."
    elif n == 6:
        return "You better not."
    elif n == 7:
        return "That question makes me wish I was Jared, 19. Please don't contact me again."
    elif n == 8:
        return "Of course!!! Don't fret."
    else:
        return "Why do you ask when you're aware you know the answer? Don't be in denial."


if __name__ == "__main__":
    main()
else:
    print(__name__)