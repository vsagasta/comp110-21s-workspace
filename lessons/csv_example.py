"""Example reading CVS files."""

from csv import DictReader

file_handle = open("data/weather.csv", "r", encoding="utf8")
# Returns TextIOWrapper
csv_reader = DictReader(file_handle)

# A "table" can be modeled as a list of rows, where a row
# is a dictionary with the column title as the key.
table: list[dict[str, str]] = []


for row in csv_reader:
    table.append(row)

print(table)


# When we're done reading the file, we should close it!
file_handle.close()