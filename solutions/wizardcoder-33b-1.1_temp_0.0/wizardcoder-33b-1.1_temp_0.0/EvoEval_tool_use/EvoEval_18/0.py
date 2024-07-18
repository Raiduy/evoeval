def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    if minutes == 0:
        return '0 minute'
    else:
        hours = get_hours(minutes)
        minutes = get_minutes(minutes)
        if hours == 0:
            return f'{minutes} minute' if minutes > 1 else '1 minute'
        elif minutes == 0:
            return f'{hours} hour' if hours > 1 else '1 hour'
        else:
            return f'{hours} hours, {minutes} minute' if hours > 1 and minutes > 1 else f'{hours} hour, {minutes} minute'