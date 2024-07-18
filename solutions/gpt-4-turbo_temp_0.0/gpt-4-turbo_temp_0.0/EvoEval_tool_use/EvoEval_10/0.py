from datetime import datetime


def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
def register_user(user_data: dict) -> bool:
    if not all((key in user_data for key in ['name', 'dob', 'email'])):
        return False
    if not all((user_data[key] for key in ['name', 'dob', 'email'])):
        return False
    if parse_date(user_data['dob']) is None:
        return False
    registered_users.append(user_data)
    return True