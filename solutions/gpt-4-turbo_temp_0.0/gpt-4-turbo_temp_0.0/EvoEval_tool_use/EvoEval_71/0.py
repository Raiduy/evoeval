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
    if not is_valid_date(date_of_birth) or not is_valid_date(at_date):
        return -1
    (day_birth, month_birth, year_birth) = map(int, date_of_birth.split('-'))
    (day_at, month_at, year_at) = map(int, at_date.split('-'))
    if (year_birth, month_birth, day_birth) > (year_at, month_at, day_at):
        return -1
    age = year_at - year_birth
    if month_at < month_birth or (month_at == month_birth and day_at < day_birth):
        age -= 1
    return age