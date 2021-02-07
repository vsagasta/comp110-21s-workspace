"""A vaccination calculator."""

__author__ = "730396600"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population_input: str = input("Population: ")
doses_administered_input: str = input("Doses administered: ")
doses_day_input: str = input("Doses per day: ")
percent_vacinated_input: str = input("Target percent vaccinated: ")

population: float = float(population_input)
doses_administered: float = float(doses_administered_input)
doses_day: float = float(doses_day_input)
percent_vacinated: float = float(percent_vacinated_input)

people_left: float = ((population * percent_vacinated) / 100) - (doses_administered / 2)
days_total_number: int = (round((people_left / (doses_day / 2))))
days: str = str(days_total_number)

today: datetime = datetime.today()
days_needed: timedelta = timedelta(days_total_number)
date_percent_reached: datetime = today + days_needed
date: str = date_percent_reached.strftime("%B %d, %Y")

print("We will reach " + percent_vacinated_input + "% vaccination in " + days + " days, which falls on " + date)