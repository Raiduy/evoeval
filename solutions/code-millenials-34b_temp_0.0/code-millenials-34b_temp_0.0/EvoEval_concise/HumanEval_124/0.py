
def valid_date(date):
    """
    This function checks if a given date string is valid or not. The function returns True for a valid date and False otherwise. 
    Validity is based on the following:
    1. The string is not empty.
    2. Day value ranges between 1 and 31 for months 1,3,5,7,8,10,12; 1 to 30 for months 4,6,9,11; and 1 to 29 for month 2.
    3. Month value ranges between 1 and 12.
    4. The date format should be in 'mm-dd-yyyy'.
    """
    if not date:
        return False
    regex = '^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$'
    match = re.search(regex, date)
    if match:
        day = int(match.group(2))
        month = int(match.group(1))
        year = int(match.group(3))
        if month < 1 or month > 12:
            return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False
        elif month == 2 and (day > 29 or (day == 29 and year % 4 != 0)):
            return False
        elif day > 31:
            return False
        else:
            return True
    else:
        return False