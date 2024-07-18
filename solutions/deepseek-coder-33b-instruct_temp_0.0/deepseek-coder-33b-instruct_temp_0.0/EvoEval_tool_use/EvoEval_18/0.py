def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    if minutes == 0:
        return '0 minute'
    elif minutes < 60:
        return f'{minutes} minute'
    else:
        hours = get_hours(minutes)
        remaining_minutes = get_minutes(minutes)
        if remaining_minutes == 0:
            return f'{hours} hour' if hours > 1 else '1 hour'
        else:
            return f"{hours} hour{('' if hours == 1 else 's')}, {remaining_minutes} minute{('' if remaining_minutes == 1 else 's')}"