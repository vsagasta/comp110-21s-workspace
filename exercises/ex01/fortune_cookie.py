"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396600"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print(" Your fortune cookie says...")


def fortune(n: int) -> str:
    """Given a number, return a fortune."""
    if n == 0:
        return "A dubious friend may be an enemy in camouflage."
    else:
        if n == 1:
            return "A feather in the hand is better than a bird in the air."
        else:
            if n == 2:
                return "All your hard work will soon pay off."
            else:
                if n == 3:
                    return "A short pencil is usually better than a long memory any day."
                else:
                    return "Do not make extra work for yourself."


random_value: int = randint(0, 5)


print(fortune(random_value))
print("Now, go spread positive vibes!")