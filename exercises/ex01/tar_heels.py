"""An exercise in remainders and boolean logic."""

__author__ = "730396600"


answer: str = input("Enter an int: ")
number = int(answer)
two_divisibility: int = number % 2
seven_divisibility: int = number % 7
if two_divisibility == 0 and seven_divisibility == 0:
    print("TAR HEELS")
else:
    if two_divisibility == 0 and seven_divisibility != 0:
        print("TAR")
    else:
        if two_divisibility != 0 and seven_divisibility == 0:
            print("HEELS")               
        else:
            print("CAROLINA")