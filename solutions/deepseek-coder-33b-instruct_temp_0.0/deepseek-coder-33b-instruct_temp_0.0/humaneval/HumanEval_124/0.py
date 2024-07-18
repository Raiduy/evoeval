
def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Check if the date is in the format: mm-dd-yyyy
    match = re.match(r'(\d{2})-(\d{2})-(\d{4})', date)
    if not match:
        return False

    month, day, year = map(int, match.groups())

    # Check if the months are valid
    if month < 1 or month > 12:
        return False

    # Check if the days are valid
    if day < 1 or day > 31:
        return False

    # Check for February
    if month == 2:
        if day > 29:
            return False
        # Check for leap year
        if day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            return False

    # Check for months with 30 days
    if month in [4, 6, 9, 11] and day > 30:
        return False

    return True
