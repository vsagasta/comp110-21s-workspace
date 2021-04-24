"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730396600"


class Simpy:
    """A class consisting of a list of floats."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Construct a point by giving x and y arguments."""
        self.values = values
    
    def __repr__(self) -> str:
        """Represents object as a string."""
        return f"Simpy({self.values})"

    def fill(self, number: float, repetitions: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        object: list[float] = []
        i: int = 0
        while i < repetitions:
            object.append(number)
            i += 1
        self.values = object

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        objects: list[float] = []
        if start > stop and step < 0:
            while start > stop:
                objects.append(start)
                start += step
        elif start < stop and step > 0:
            while start < stop:
                objects.append(start)
                start += step
        else:
            objects = []
        self.values = objects

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""    
        total: float = 0
        for number in self.values:
            total += number
        return round(total, 5)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads the addition operator to use with Simpy's and floats."""
        added_values: list[float] = []
        if isinstance(rhs, float):
            for number in self.values:
                added_values.append(number + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                added_values.append(self.values[i] + rhs.values[i])
        return Simpy(added_values)
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads the power operator to use with Simpy's and floats."""
        pow_values: list[float] = []
        if isinstance(rhs, float):
            for number in self.values:
                pow_values.append(number ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                pow_values.append(self.values[i] ** rhs.values[i])
        return Simpy(pow_values)

    def __mod__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads the modulo remainder operator to use with Simpy's and floats."""
        mod_values: list[float] = []
        if isinstance(rhs, float):
            for number in self.values:
                mod_values.append(number % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mod_values.append(self.values[i] % rhs.values[i])
        return Simpy(mod_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the equality operator to make masks with Simpy's and floats."""
        mask_values: list[bool] = []
        if isinstance(rhs, float):
            for number in self.values:
                mask_values.append(number == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mask_values.append(self.values[i] == rhs.values[i])
        return mask_values

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the equality operator to make masks with Simpy's and floats."""
        mask_values: list[bool] = []
        if isinstance(rhs, float):
            for number in self.values:
                mask_values.append(number > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mask_values.append(self.values[i] > rhs.values[i])
        return mask_values

    def __getitem__(self, rhs: Union[list[bool], int]) -> Union[Simpy, float]:
        """Overloads subscription notation."""
        mask_values: list[float] = []
        if isinstance(rhs, list):
            assert len(self.values) == len(rhs)
            for i in range(len(self.values)):
                if rhs[i]:
                    mask_values.append(self.values[i])
            return Simpy(mask_values)
        else:
            if rhs >= len(self.values):
                raise IndexError
            else:
                return self.values[rhs]