def is_valid_date(date: str) -> bool:
    """
    Check if the given date string is valid.
    """
    # split the date string into day, month, year parts
    day, month, year = date.split('/')

    # check if day, month, year are all digit strings
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    # convert day, month, year to integers
    day = int(day)
    month = int(month)
    year = int(year)

    # check if month is in valid range
    if not 1 <= month <= 12:
        return False

    # check if day is in valid range
    if not 1 <= day <= 31:
        return False

    # check if year is in valid range
    if not 1900 <= year <= 2100:
        return False

    return True
def birthday_on_a_weekday(birthdate: str, year: int) -> str:
    """
    Given a birthdate (in the format DD/MM/YYYY) and a year (e.g. 2022),
    return the day of the week the birthday falls on in the specified year.
    A valid birth year should be in the range 1900 to 2100 (inclusive).
    If the birthdate or year is not valid, return 'Invalid date or year'.

    >>> birthday_on_a_weekday('02/02/2000', 2022)
    'Wednesday'
    >>> birthday_on_a_weekday('31/11/2000', 2022)
    'Invalid date or year'
    """
    if not is_valid_date(birthdate) or not 1900 <= year <= 2100:
        return 'Invalid date or year'
    (day, month, year) = map(int, birthdate.split('/'))
    day_of_week = (year - 1900) % 7
    for i in range(year - 1900):
        if (i + 1900) % 4 == 0 and (i + 1900) % 100 != 0 or (i + 1900) % 400 == 0:
            day_of_week += 1
    day_of_week += (year - 1900) // 4 - (year - 1900) // 100 + (year - 1900) // 400
    day_of_week += 13 * (month + 1) // 5 % 7
    day_of_week += day - 1
    day_of_week %= 7
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day_of_week]