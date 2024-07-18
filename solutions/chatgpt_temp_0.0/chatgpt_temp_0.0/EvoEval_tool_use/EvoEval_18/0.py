def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    hours = get_hours(minutes)
    mins = get_minutes(minutes)
    if hours == 0 and mins == 0:
        return '0 minute'
    elif hours == 0:
        return f"{mins} minute{('s' if mins != 1 else '')}"
    elif mins == 0:
        return f"{hours} hour{('s' if hours != 1 else '')}"
    else:
        return f"{hours} hour{('s' if hours != 1 else '')}, {mins} minute{('s' if mins != 1 else '')}"