"""EX03 - prime functions."""

from typing import List

__author__: str = "730396600"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(5))
    print(list_primes(10, 20))


def is_prime(number: int) -> bool:
    """A function that determines wether the number given is prime or not."""
    i: int = 2
    if number <= 1:
        return(False)
    else:
        while i < number:
            if number % i == 0:
                return(False)
            else:
                i += 1
        return(True)


def list_primes(start: int, stop: int) -> list[int]:
    """A function that return a list of all prime numbers between the first parameter and the second."""
    all_primes: List[int] = []
    not_primes: List[int] = []
    parameters: range = range(start, stop)
    for item in parameters:
        if is_prime(item):
            all_primes.append(item)
        else:
            not_primes.append(item)
    return all_primes


if __name__ == "__main__":
    main()