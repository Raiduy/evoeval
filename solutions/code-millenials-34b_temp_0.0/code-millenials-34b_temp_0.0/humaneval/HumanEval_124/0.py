
def valid_date(date):
    # Check if the date is in the correct format and not empty
    if not re.match("\d{2}-\d{2}-\d{4}", date):
        return False
    
    # Split the date into month, day, and year
    month, day, year = map(int, date.split('-'))
    
    # Check the validity of the month
    if month < 1 or month > 12:
        return False
    
    # Check the validity of the day
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2 and (day < 1 or day > 29):
        return False
    
    # Check if the year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and day > 29:
        return False
    
    return True
