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
        return '9999-12-31'
    if month == 2 and day == 28:
        if is_leap_year(year):
            return f'{year}-{month:02d}-{day + 1:02d}'
        else:
            return 'Invalid date'
    if month == 2 and day == 29:
        return f'{year}-{month + 1:02d}-01'
    if day == 31:
        if month == 1 or month == 3 or month == 5 or (month == 7) or (month == 8) or (month == 10):
            return f'{year}-{month + 1:02d}-01'
        else:
            return f'{year + 1}-01-01'
    return f'{year}-{month:02d}-{day + 1:02d}'