
def valid_date(date):
    """
    This function checks if a given date string is valid or not. The function returns True for a valid date and False otherwise. 
    Validity is based on the following:
    1. The string is not empty.
    2. Day value ranges between 1 and 31 for months 1,3,5,7,8,10,12; 1 to 30 for months 4,6,9,11; and 1 to 29 for month 2.
    3. Month value ranges between 1 and 12.
    4. The date format should be in 'mm-dd-yyyy'.
    
    Example:
    valid_date('03-11-2000') => True
    valid_date('15-01-2012') => False
    valid_date('04-0-2040') => False
    valid_date('06-04-2020') => True
    valid_date('06/04/2020') => False
    """
    if not date:
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    (month, day, year) = parts
    if not month.isdigit() or not day.isdigit() or (not year.isdigit()):
        return False
    month = int(month)
    day = int(day)
    year = int(year)
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    return True