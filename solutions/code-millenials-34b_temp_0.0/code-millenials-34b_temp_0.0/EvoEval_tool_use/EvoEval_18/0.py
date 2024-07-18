def get_hours(minutes: int) -> int:
    return minutes // 60

def get_minutes(minutes: int) -> int:
    return minutes % 60
def format_duration(minutes: int) -> str:
    if minutes == 0:
        return '0 minute'
    hours = get_hours(minutes)
    mins = get_minutes(minutes)
    if hours == 1:
        h_str = '1 hour'
    else:
        h_str = f'{hours} hours'
    if mins == 1:
        m_str = '1 minute'
    else:
        m_str = f'{mins} minutes'
    if hours == 0:
        return m_str
    elif mins == 0:
        return h_str
    else:
        return f'{h_str}, {m_str}'