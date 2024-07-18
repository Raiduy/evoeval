def is_leap_year(year: int) -> bool:
    """ Returns True if the year is a leap year, False otherwise. """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def get_days_in_month(month: int, year: int) -> int:
    """ Returns the number of days in a month for a given year. """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 30
from typing import List

def filter_by_valid_dates(dates: List[str]) -> List[str]:
    """ Filters an input list of strings and returns only those that are valid dates in the format 'YYYY-MM-DD'.
    >>> filter_by_valid_dates(['2020-02-30', '2020-02-29', '2019-02-29', '2019-12-31'])
    ['2020-02-29', '2019-12-31']
    """
    valid_dates = []
    for date in dates:
        try:
            (year, month, day) = map(int, date.split('-'))
            if get_days_in_month(month, year) >= day:
                valid_dates.append(date)
        except ValueError:
            pass
    return valid_dates