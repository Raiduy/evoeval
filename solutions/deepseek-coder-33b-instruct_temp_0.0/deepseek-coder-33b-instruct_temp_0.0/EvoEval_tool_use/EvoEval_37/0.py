def parse_time(time_str: str) -> tuple:
    """
    This function takes a string time in the format "HH:MM" and parses it into a tuple of integers.
    :param time_str: a string representing time in 24 hour format "HH:MM"
    :return: a tuple (hours, minutes)
    >>> parse_time("12:30")
    (12, 30)
    >>> parse_time("23:15")
    (23, 15)
    """
    hours, minutes = map(int, time_str.split(':'))
    return hours, minutes
def time_to_minutes(time_list: list) -> list:
    """
    This function takes a list of time strings in the format "HH:MM" and converts each time into minutes past midnight.
    The function returns a list of integers where each integer represents the minutes past midnight corresponding to the respective time string in the input list.
    >>> time_to_minutes(["00:00", "12:00", "23:59"])
    [0, 720, 1439]
    >>> time_to_minutes(["01:00", "13:00", "14:15"])
    [60, 780, 855]
    """
    return [hours * 60 + minutes for (hours, minutes) in map(parse_time, time_list)]