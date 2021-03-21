
from typing import List

def main() -> None:

    b: List[str] = a
    
    f(a)
    print(a)
    print(b)
    g()
    print(b[0])

def f(a: list[str]) -> None:
    a[0] = "p"
    
    a = ["m", "j"]
    print(a)
    


def g() -> None:
    global a
    a[1] = "y"
    a = ["k", "g"]


a: list[str] = ["w", "u"]

if __name__ == "__main__":
    main()