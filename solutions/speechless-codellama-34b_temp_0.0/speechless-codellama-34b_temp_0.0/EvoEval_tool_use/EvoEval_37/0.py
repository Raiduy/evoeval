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
    """
    minutes_list = []
    for time_str in time_list:
        (hours, minutes) = parse_time(time_str)
        total_minutes = hours * 60 + minutes
        minutes_list.append(total_minutes)
    return minutes_list