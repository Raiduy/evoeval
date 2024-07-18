def is_valid_date(date_string):
    '''
    A helper function to check if a given string is a valid date in format "dd-mm-yyyy"
    Returns True if valid, False otherwise
    '''
    day, month, year = date_string.split('-')
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return False
    d, m, y = int(day), int(month), int(year)
    if m < 1 or m > 12 or d < 1 or d > 31:
        return False
    if m in [4, 6, 9, 11] and d > 30:
        return False
    if m == 2 and (d > 29 or (d > 28 and (y % 4 != 0 or (y % 100 == 0 and y % 400 != 0)))):
        return False
    return True
def get_age_at_date(date_of_birth, at_date):
    """
    Given a person's date of birth and a specific date, both in the format "dd-mm-yyyy", 
    return the age of the person at the specific date in years rounded down to the nearest whole 
    year. If the dates are not valid or the date of birth comes after the specific date, return -1.
    Example:
    get_age_at_date("01-01-2000", "01-01-2020") == 20
    get_age_at_date("01-01-2020", "01-01-2000") == -1
    get_age_at_date("01-01-2000", "01-02-2020") == 20
    get_age_at_date("01-01-2000", "31-12-2019") == 19
    """
    if not is_valid_date(date_of_birth) or not is_valid_date(at_date):
        return -1
    (dob_day, dob_month, dob_year) = map(int, date_of_birth.split('-'))
    (at_day, at_month, at_year) = map(int, at_date.split('-'))
    if at_year < dob_year or (at_year == dob_year and (at_month < dob_month or (at_month == dob_month and at_day < dob_day))):
        return -1
    age = at_year - dob_year
    if (at_month, at_day) < (dob_month, dob_day):
        age -= 1
    return age