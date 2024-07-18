from datetime import datetime


def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
def register_user(user_data: dict) -> bool:
    if 'name' not in user_data or 'dob' not in user_data or 'email' not in user_data:
        return False
    if not user_data['name'] or not user_data['email']:
        return False
    dob = parse_date(user_data['dob'])
    if dob is None:
        return False
    return True