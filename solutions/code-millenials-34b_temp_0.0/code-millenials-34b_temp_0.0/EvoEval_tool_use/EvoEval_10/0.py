from datetime import datetime


def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
def register_user(user_data: dict) -> bool:
    if 'name' in user_data and 'dob' in user_data and ('email' in user_data):
        if user_data['name'] and user_data['email']:
            dob = parse_date(user_data['dob'])
            if dob:
                return True
    return False