def check_date(date):
    """
    Helper function to check if a given date string is valid or not
    Input: string in the format 'yyyy-mm-dd'
    Output: True if the date is valid, False otherwise
    """
    import datetime
    try:
        year, month, day = map(int, date.split('-'))
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False
def calculate_duration(dates):
    """You are given a list of dates in 'yyyy-mm-dd' format.
    You need to find the oldest and the most recent date in the list, and return the difference between them in days.

    Assumptions:
    1. All dates in the list are valid dates in 'yyyy-mm-dd' format
    2. The list contains at least two different dates

    Examples:
    For dates = ['2021-01-01', '2021-12-31'] the output should be 364
    For dates = ['2021-12-31', '2020-12-31'] the output should be 365
    For dates = ['2019-06-01', '2018-06-01', '2020-06-01'] the output should be 731
    For dates = ['2022-08-01', '2022-09-01', '2022-07-01'] the output should be 62
    """
    import datetime
    date_objects = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]
    oldest_date = min(date_objects)
    most_recent_date = max(date_objects)
    duration = (most_recent_date - oldest_date).days
    return duration