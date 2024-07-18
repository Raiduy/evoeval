def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    """
    Convert a given amount of minutes to a formatted duration string in the format 'H hours, M minutes'.
    If the number is zero, it should return '0 minute'.
    It should only return the units that are non-zero (e.g. '1 minute', '2 hours', etc.)
    Note whether to put (s) depends on the amount
    """
    if minutes == 0:
        return '0 minute'
    hours = get_hours(minutes)
    mins = get_minutes(minutes)
    hour_str = f"{hours} hour{('s' if hours != 1 else '')}" if hours > 0 else ''
    minute_str = f"{mins} minute{('s' if mins != 1 else '')}" if mins > 0 else ''
    if hours > 0 and mins > 0:
        return f'{hour_str}, {minute_str}'
    elif hours > 0:
        return hour_str
    else:
        return minute_str