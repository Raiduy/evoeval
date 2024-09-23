
def valid_date(date):
    if not date:
        return False

    if len(date.split('-')) != 3:
        return False

    month, day, year = date.split('-')

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2 and day > 29:
        return False

    return True
