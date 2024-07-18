def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    hours = get_hours(minutes)
    minutes = get_minutes(minutes)
    if hours == 0 and minutes == 0:
        return '0 minute'
    result = []
    if hours > 0:
        result.append(f'{hours} hour')
        if hours > 1:
            result[-1] += 's'
    if minutes > 0:
        result.append(f'{minutes} minute')
        if minutes > 1:
            result[-1] += 's'
    return ', '.join(result)