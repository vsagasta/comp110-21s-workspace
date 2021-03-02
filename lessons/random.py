from typing import List

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

print(score(1))
print(score(7))
print(score(2))