"""Utility functions for wrangling data."""

__author__ = "730396600"


from _typeshed import SupportsDivMod
from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for line in csv_reader:
        rows.append(line)
    file_handle.close()
    return rows
    

def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column whose name is the second parameter."""
    age: list[str] = []
    for item in rows:
        age.append(item[column])
    return age


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""
    table: dict[str, list[str]] = {}
    for item in rows[0]:
        data: list[str] = column_values(rows, item)
        table[item] = data
    return table


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first rows visible."""
    first_key: str = list(table.keys())[0]
    if len(table[first_key]) <= n:
        return table
    else:
        table_head: dict[str, list[str]] = {}
        for item in table:
            data: list[str] = []
            i: int = 0
            while n > i:
                data.append(table[item][i])
                i += 1
            table_head[item] = data
        return table_head


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a subset of the original columns."""
    short_table: dict[str, list[str]] = {}
    i: int = 0
    while len(columns) > i:
        if columns[i] in table:
            data: list[str] = table[columns[i]]
            short_table[columns[i]] = data
        i += 1
    return short_table


def count(values: list[str]) -> dict[str, int]:
    """This will produce a dictionary where each key is the number of times that value appeared."""
    counts: dict[str, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def comp(col: list[str]) -> list[bool]:
    """A mask function that returns a list of bools."""
    result: list[bool] = []
    for item in col:
        if item == "No":
            result.append(False)
        else:
            result.append(True)
    return result


def masked(col: list[str], mask: list[bool]) -> list[str]:
    """From a column and list, returns values in the input where the list value is true."""
    result: list[str] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


def bool_count(values: list[bool]) -> dict[bool, int]:
    """This will produce a dictionary where each key is the number of times that value appeared."""
    counts: dict[bool, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def flip(data: list[bool]) -> list[bool]:
    """A function that that reverses True and false values in a bool list."""
    flipped: list[bool] = []
    for item in data:
        flipped.append(not item)
    return flipped
    

def proportion(grades: dict[str, int], total: int) -> dict[str, float]:
    prop: dict[str, float] = {}
    for item in grades:
        new: float = round((grades[item] / total) * 100, 2)
        prop[item] = new
    return prop