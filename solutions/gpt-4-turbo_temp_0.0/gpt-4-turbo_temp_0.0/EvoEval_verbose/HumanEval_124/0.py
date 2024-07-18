
def valid_date(date):
    if not date:
        return False
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        (month, day, year) = parts
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 29
    if day < 1 or day > max_day:
        return False
    return True