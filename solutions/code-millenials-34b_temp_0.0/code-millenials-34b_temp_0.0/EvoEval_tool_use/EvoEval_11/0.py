def is_valid_date(date: str) -> bool:
    """ 
    Helper function to check if a date string is valid. 
    The date string should be in the format of 'YYYY-MM-DD'.
    Returns True if the date string is valid, False otherwise.
    """
    try:
        year, month, day = map(int, date.split('-'))
        return 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        return False

def is_leap_year(year: int) -> bool:
    """
    Helper function to check if a year is a leap year.
    Returns True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_next_day(date: str) -> str:
    """
    Function that takes a date string in the format 'YYYY-MM-DD'
    and returns a string representation of the next date.
    
    If the date string is invalid or the date is '9999-12-31', the function should return 'Invalid date'.
    
    >>> get_next_day('2018-12-31')
    '2019-01-01'
    
    >>> get_next_day('2020-02-28')
    '2020-02-29'
    
    >>> get_next_day('2020-02-29')
    '2020-03-01'
    
    >>> get_next_day('2020-12-31')
    '2021-01-01'
    
    >>> get_next_day('9999-12-31')
    'Invalid date'
    """
    if not is_valid_date(date) or date == '9999-12-31':
        return 'Invalid date'
    (year, month, day) = map(int, date.split('-'))
    if month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
    elif day == 31 and month in [4, 6, 9, 11]:
        month += 1
        day = 1
    elif day == 30 and month == 2:
        if is_leap_year(year):
            day = 29
        else:
            month += 1
            day = 1
    elif day == 29 and month == 2:
        if is_leap_year(year):
            day = 28
        else:
            month += 1
            day = 1
    else:
        day += 1
    return f'{year:04d}-{month:02d}-{day:02d}'