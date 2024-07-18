
def valid_date(date):
    if not date:
        return False

    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False

    month, day, year = date_parts
    if not re.match('^\d{2}$', month) or not re.match('^\d{2}$', day) or not re.match('^\d{4}$', year):
        return False

    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if day > 29:
            return False
        if day == 29 and year % 4 != 0:
            return False
        if day == 29 and year % 100 == 0 and year % 400 != 0:
            return False

    return True
