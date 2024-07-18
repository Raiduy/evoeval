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
    minutes1 = convert_to_minutes(time1)
    minutes2 = convert_to_minutes(time2)
    if minutes2 < minutes1:
        minutes2 += 24 * 60
    return minutes2 - minutes1