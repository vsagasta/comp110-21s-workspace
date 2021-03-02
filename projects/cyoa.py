"""A game to learn some DBT therapy skills."""

__author__ = "730396600"


from typing import List
from random import randint

WINK_EMOJI: str = "\U0001F609"
SAD_EMOJI: str = "\U0001F622"
HAPPY_EMOJI: str = "\U0001F601"
ANGRY_EMOJI: str = "\U0001F621"
FEAR_EMOJI: str = "\U0001F628"
SURPRISE_EMOJI: str = "\U0001F632"
LOVE_EMOJI: str = "\U0001F970"

player: str
points: int


def main() -> None:
    """Entrypoint of the game."""
    global points
    points = 0
    greet()
    playing: bool = True
    """This while loop works to keep the game running until the player quits."""
    """Works to fulfil requirement 9 in the rubrick."""
    while playing:
        print("You have four different paths you can go from here. You can ")
        print("(A) go to the mindfulness module.")
        print("(B) go to interpersonal effectiveness module.")
        print("(C) go to the emotion regulation module.")
        print("(D) abandon the game.")
        path: str = input("Where do you want to go? ")
        if path.lower() == "a":
            mindfulness()
            points += score(0)
            point_list.clear()
        elif path.lower() == "b":
            interpersonal_effectiveness()
            points += score(0)
            point_list.clear()
            print(f"Your point total for all modules is {points}.")
        elif path.lower() == "c":
            emotion_regulation()
            points += score(0)
            point_list.clear()
        elif path.lower() == "d":
            answer: str = input("Are you sure? ")
            playing = "no" == answer.lower()
        else:
            print("Invalid answer. Please type A, B, C, or D as your answer.")
            playing = True
    points += score(0)
    point_list.clear()
    print(f"You accumulated {points} points while going through the modules.")
    print(f"Use the skills learned often and wisely. Goodbye {player}!")


def greet() -> None:
    """A procedure that welcomes the player and assigns their name to a player variable."""
    print("Hello! Welcome to your virtual DBT skills lesson.")
    print("Today you will be able to look through the different modules and learn how to use various skills.")
    global player
    player = input("Before we start, what's your name? ")
    print(f"Okay {player}. Lets get started.")


point_list: List[int] = list()


def score(n: int) -> int:
    """A function that keeps track of a players points as he works through the modules."""
    point_list.append(n)
    length: int = len(point_list)
    i: int = 0
    total: int = 0
    while i < length:
        total += point_list[i]
        i += 1
    return total


def mindfulness() -> None:
    """A procedure that walks you through the mindfulness module."""
    print("Mindfulness is the act of conciously focusing in the present, ")
    print("without judgement, and without attachement to the moment.")
    print("Our fisrt set of skills are our 'what' skills. There are three total and they are")
    print("A - OBSERVE: notice your body sensations, pay attention to the present, and control your attention.")
    print("B - DESCRIBE: put words on your current experience / thoughts, and labeling what you observe.")
    print("C - PARTICIPATE: throw yourself completely into activities of the current moment and go with the flow.")
    global points
    points += 3
    print(f"Great! You've earned three points for learning those three skills {player}.")
    print("Now keep earnning more by working through a few practice questions.")
    print("Laying on the grond watching clouds and writting down the shapes you see.")
    response: str = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "b":
        print(f"Congratulations! You are right {player}. The skill described was B.")
        points += 3
    else:
        while response.lower() != "b":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print("Singing in the shower.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "c":
        print(f"Congratulations! You are right {player}. The skill described was C.")
        points += 3
    else:
        while response.lower() != "c":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print("Saying out loud the emotion you are currently feeling.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "b":
        print(f"Congratulations! You are right {player}. The skill described was B.")
        points += 3
    else:
        while response.lower() != "b":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print("Putting a piece of chocolate in your mouth and only focusing on its taste.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "a":
        print(f"Congratulations! You are right {player}. The skill described was A.")
        points += 3
    else:
        while response.lower() != "a":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print("Noticing your body's reaction to holding an ice cube in your hand.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "a":
        print(f"Congratulations! You are right {player}. The skill described was A.")
        points += 3
    else:
        while response.lower() != "a":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print("Fully immerse yourself in what another person is saying.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "c":
        print(f"Congratulations! You are right {player}. The skill described was C.")
        points += 3
    else:
        while response.lower() != "c":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Final one!")
    print("Sitting on a bench at a park, observe and mention one thing you notice about every person that walks by.")
    response = input("Answer A, B, or C for whichever skill you think the situation is describing: ")
    if response.lower() == "b":
        print(f"Congratulations! You are right {player}. The skill described was B.")
        points += 3
    else:
        while response.lower() != "b":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Which skill is this situation describing? A, B, or C? ")
        print("Correct.")
        points += 1
    print(f"Congratulations {player}! Your point total is {points}.")
    print("Now here is a random exercise you can practice mindfulness with:")
    random_number: int = randint(0, 10)
    print(mindfulness_practice(random_number))
    print(f"Lets get you back to the home page so you can keep working through modules {WINK_EMOJI}.")


def mindfulness_practice(n: int) -> str:
    """A function that gives you a practice exercise in response to an integer."""
    if n == 0:
        return "Dance to music"
    elif n == 1:
        return "Observe your breath going in and out."
    elif n == 2:
        return "For a couple minutes, each time you inhale and exhale mention it out loud."
    elif n == 3:
        return "Say a word again and again, noticing how your body moves."
    elif n == 4:
        return "Fill in the blanks to this sentence: I feel ____ and my thoughts are ____."
    elif n == 5:
        return "Fill in the blanks to this sentence: When ____ occurs, I feel ____ and my thoughts are ____."
    elif n == 6:
        return "Immerse yourself in a Hank Green lesson video."
    elif n == 7:
        return "Play karaoke with friends."
    elif n == 8:
        return "Close your eyes and notice the sensations occuring in your body in the present moment."
    else:
        return "Fully immerse yourself in a game of chess."

    
def interpersonal_effectiveness() -> None:
    """A procedure that walks you through the interpersonal effectiveness module."""
    print("Interpersonal effectiveness skills help you build new relationships, ")
    print("strengthen current ones, and effectively deal with conflict situations.")
    print("There are a lot of myths surrounding interpersonal relationships. Lets take a look at some common ones.")
    print("Answer 'T' for True and 'F' for False depending on your thoughts about the next few statements.")
    print("Other people's reactions can prevent an interaction from being effective.")
    response: str = input("Do you think the statement is True (T) or False (F)? ")
    if response.lower() == "t":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "t":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Next one!")
    print("If I make a request, this will show that I am a weak person.")
    response = input("Do you think the statement is True (T) or False (F)? ")
    if response.lower() == "f":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "f":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Next one!")
    print("Being right is the most imprtant thing in relationships.")
    response = input("Do you think the statement is True (T) or False (F)? ")
    if response.lower() == "f":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "f":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Next one!")
    print("Your interactions are innefective because you forget long-term goals for short-term ones.")
    response = input("ADo you think the statement is True (T) or False (F)? ")
    if response.lower() == "t":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "t":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Next one!")
    print("I don't deserve to have my needs met by other people.")
    response = input("Do you think the statement is True (T) or False (F)? ")
    if response.lower() == "f":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "f":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Next one!")
    print("I have to know whether a person is going to say yes before I make a request.")
    response = input("Do you think the statement is True (T) or False (F)? ")
    if response.lower() == "f":
        print(f"Congratulations {player}! You are right.")
        score(2)
    else:
        while response.lower() != "f":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Your point total is {score(0)}.")
    print("Final one!")
    print("Sometimes, getting what I want is more important than mantaining the relationship.")
    response = input("ADo you think the statement is True (T) or False (F)? ")
    if response.lower() == "t":
        print(f"Congratulations {player}! You are right.")
        print("Sometimes gaining self-respect will take precedence over maintaining the raltionship.")
        score(2)
    else:
        while response.lower() != "t":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("Do you think the statement is True (T) or False (F)? ")
        print("Correct.")
        score(1)
    print(f"Good job on that exercise! You now have {score(0)} points.")
    print("A very important thing to consider in interpersonal relationships is ")
    print("wether the relationship is good or bad for your overall well being.")
    print("If the relationship in question is good, you should strive to keep it and nourish it.")
    print("However, when problems arise, it is important to be able to discern ")
    print("wether the relationship is an interfering one, or a destructive one.")
    print("An interfering relationship is one that blocks or makes it difficult to ")
    print("pursue goals important to you such as other relationships, or enjoyable activities.")
    print("A destructive relationship has the quality of destroying or completely spoiling the quality ")
    print("of the relationship and / or aspects of yourself such as safety, self-esteem, or integrity.")
    score(2)
    print("Now lets imagine that you are having problems with two different friends and have come to the ")
    print("conclusion that one of those relationships is destructive and the other is interfering.")
    print(f"{player}, what do you think you should do? Should you ")
    print("A - make sure you cut both your friends out of your life")
    print("B - try to problem solve your interpersonal issues with both.")
    print("C - end the destructive relationship and try to problem solve the interfering relationship.")
    print("D - end the interfering relationship and try to problem solve the destructive one.")
    print("E - continue as if nothing happened")
    print("F - end the destructive relationship and allow the interfering relationship to get better alone with time.")
    response = input("Your answer: ")
    if response.lower() == "c":
        print(f"Congratulations {player}! You are right.")
        print("Destructive relationships are past the point of problem solving, and if you want to keep your second")
        print("friend, you should make a concious effort for the interfering relationship to become a healthier one.")
        score(5)
    else:
        while response.lower() != "c":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input("What should you do with your two friends? A, B, C, D, E, or F? ")
        print("Correct.")
        print("Destructive relationships are past the point of problem solving, and if you want to keep your second")
        print("friend, you should make a concious effort for the interfering relationship to become a healthier one.")
        score(1)
    print(f"Congratulations! Your point total for this module is {score(0)}.")
    print(f"Lets get you back to the home page so you can keep working through modules {WINK_EMOJI}.")


def emotion_regulation() -> None:
    """A procedure that walks you through the emotion regulation module."""
    """An extra path that meets the specifications for above and beyond specification 10."""
    global points
    print("Emotion regulation helps reduce emotional suffering,")
    print("not by getting rid of emotions, but by changing them and reducing their intensity.")
    print(f"{player} an important part of emotion regulation is learning to identify and")
    print("name emotions so you know how to deal with them better, so lets practice with an exercise.")
    print("Next I will show you an emoji. Your goal is to correctly identify the emotion expressed in its face.")
    print("Lets get started!")
    print(f"Is this {ANGRY_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response: str = input("Your answer: ")
    if response.lower() == "c":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "c":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {ANGRY_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print(f"Is this {SURPRISE_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response = input("Your answer: ")
    if response.lower() == "e":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "e":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {SURPRISE_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print(f"Is this {HAPPY_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response = input("Your answer: ")
    if response.lower() == "b":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "b":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {HAPPY_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print(f"Is this {LOVE_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response = input("Your answer: ")
    if response.lower() == "f":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "f":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {LOVE_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Next one!")
    print(f"Is this {SAD_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response = input("Your answer: ")
    if response.lower() == "a":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "a":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {SAD_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print("Last one!")
    print(f"Is this {FEAR_EMOJI} emoji exemplifying")
    print("A - sadness.")
    print("B - happiness.")
    print("C - anger.")
    print("D - fear.")
    print("E - surprise.")
    print("F - love.")
    response = input("Your answer: ")
    if response.lower() == "d":
        print(f"Congratulations {player}! You are right.")
        points += 3
    else:
        while response.lower() != "d":
            print(f"I'm sorry, that's incorrect {player}. Try again.")
            response = input(f"What emotion is this {FEAR_EMOJI} emoji exemplifying? A, B, C, D, E, or F? ")
        print("Correct.")
        points += 1
    print(f"Your point total is {points}.")
    print(f"Lets get you back to the home page so you can keep working through modules {WINK_EMOJI}.")


if __name__ == "__main__":
    main()
else:
    print(__name__)