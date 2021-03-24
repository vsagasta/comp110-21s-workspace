"""Utility functions for wrangling data."""

__author__ = "730396600"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    for line in csv_file:
        print(line[0])
        #rows.append(line)
    print(rows)
    return rows


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column whose name is the second parameter."""


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""


def head(data: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first rows visible."""


def select(data: dict[str, list[str]], columns:list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a subset of the original columns."""


def count(values:list[str]) -> dict[str, int]:
    """This will produce a dictionary where each key is the number of times that value appeared."""

    
    
    
    
    
"""
raw_row_number,
date,
time,
location,
county_name,
subject_age,
subject_race,
subject_sex,
officer_id_hash,
department_name,
type,
arrest_made,
citation_issued,
warning_issued,
outcome,
contraband_found,
contraband_drugs,
contraband_weapons,
frisk_performed,
search_conducted,
search_person,
search_vehicle,
search_basis,
reason_for_frisk,
reason_for_search,
reason_for_stop,
raw_Ethnicity,
raw_Race,
raw_action_description.
"""