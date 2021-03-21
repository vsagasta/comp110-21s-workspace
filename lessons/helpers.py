"""Example functions that can be imported elsewhere."""

THE_ANSWER: int = 42

def shout(message: str) -> None:
    print(message.upper())

def whisper(message: str) -> None:
    print(message.lower())

print("helpers.py was evaluated")