def convert_to_minutes(time):
    """
    Converts the time from "HH:MM" format to minutes
    """
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes
def time_difference(time1, time2):
    """
    Given two times in "HH:MM" format, find the difference in minutes between the two times.
    If the second time is earlier than the first, it is assumed that the second time is on the next day.
    Both time1 and time2 are assumed to be valid times.
    Return the difference in minutes.
    """
    time1_in_minutes = convert_to_minutes(time1)
    time2_in_minutes = convert_to_minutes(time2)
    if time2_in_minutes < time1_in_minutes:
        time2_in_minutes += 24 * 60
    return time2_in_minutes - time1_in_minutes