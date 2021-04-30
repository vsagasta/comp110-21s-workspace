"""Examples of vectorized operations on StrArray."""

from __future__ import annotations

from typing import Union

class StrArray:
    """Utility class for working with sequences of strings."""

    values: list[str]

    def __init__(self, values: list[str]) -> None:
        self.values = values

    def __repr__(self) -> str:
        return f"StrArray({self.values})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return StrArray(result)

    
s: StrArray = StrArray(["a", "b", "c"])
t: StrArray = StrArray(["d", "e", "f"])
print(s + "?")
print(t)