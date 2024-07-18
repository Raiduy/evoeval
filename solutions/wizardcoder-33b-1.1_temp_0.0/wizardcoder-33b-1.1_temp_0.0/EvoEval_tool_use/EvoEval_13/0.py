def is_valid_date(date: str) -> bool:
    """
    Helper function to check if the given date string is valid or not. 
    The date string should be in yyyy-mm-dd format. 
    Return True if the date is valid, False otherwise.

    >>> is_valid_date("2021-09-30")
    True
    >>> is_valid_date("2021-02-29")
    False
    """
    year, month, day = (int(i) for i in date.split('-'))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 28 + (1 if year%400 == 0 or (year%4 == 0 and year%100 != 0) else 0):
        return False
    return True


def is_leap_year(year: int) -> bool:
    """
    Helper function to check if the given year is a leap year or not.
    Return True if the year is a leap year, False otherwise.

    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2021)
    False
    """
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)
def days_between_dates(date1: str, date2: str) -> int:
    """
    Return the number of days between two dates date1 and date2. 
    The dates should be in yyyy-mm-dd format. If any or both of the 
    dates are invalid, return -1. If date2 is before date1, return -2.

    >>> days_between_dates("2021-09-30", "2021-10-01")
    1
    >>> days_between_dates("2021-02-29", "2021-03-01")
    -1
    >>> days_between_dates("2021-10-01", "2021-09-30")
    -2
    """
    if not is_valid_date(date1) or not is_valid_date(date2):
        return -1
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    if date2 < date1:
        return -2
    return (date2 - date1).days