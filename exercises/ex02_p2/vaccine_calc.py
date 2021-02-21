"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730396600"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    date: str = future_date(days)
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + date)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Function that tells you how many days it will take to vaccinate the desired population."""
    people_left: float = ((population * target) / 100) - (doses / 2)
    days_total_number: int = (round((people_left / (doses_per_day / 2))))
    return(days_total_number)


def future_date(days_total_number: int) -> str:
    """Function that gives the date target population will be fully vaccinated."""
    today: datetime = datetime.today()
    days_needed: timedelta = timedelta(days_total_number)
    date_percent_reached: datetime = today + days_needed
    date_vaccinated: str = date_percent_reached.strftime("%B %d, %Y")
    return(date_vaccinated)


if __name__ == "__main__":
    main()
