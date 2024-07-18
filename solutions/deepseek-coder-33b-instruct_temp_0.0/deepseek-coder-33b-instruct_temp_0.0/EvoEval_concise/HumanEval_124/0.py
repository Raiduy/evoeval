
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
    match = re.match('(\\d{2})-(\\d{2})-(\\d{4})', date)
    if not match:
        return False
    (month, day, year) = map(int, match.groups())
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if day > 29:
            return False
        if day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    return True