"""Example of elif statements."""


RIGHT_ANSWER: int = 42


print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == RIGHT_ANSWER:
    print("Correct!")
    print("Great work!")
elif guess > RIGHT_ANSWER:
    print("Too high.")
else:
    print("Too low.")


print("Game Over")