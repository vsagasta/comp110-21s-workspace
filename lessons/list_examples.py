"""Some examples of list cncepts."""

from random import randint


rolls: list[int]

rolls = [2, 3, 2, 6]
print(rolls)

print(f"Length of rolls is {len(rolls)}")
print(f"The last value in the list is {rolls[len(rolls) - 1]}")

print(rolls)
rolls.append(randint(1, 6))
print(rolls)

rolls.pop() #List's pop method, with no argument, removes the last item of the list
rolls.pop(0) #List's pop method pop a specific index
print(rolls)

words: list[str] = list() #Construct an empty list using the list constructor
words.append("Hello")
print(words)