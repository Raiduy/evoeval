def validate_input(data: dict):
    """ Check if the input contains 'name' and 'age' as keys and returns True if exists.

    >>> validate_input({'name': 'John', 'age': 23})
    True
    >>> validate_input({'name': 'John', 'height': 170})
    False
    """
    return 'name' in data and 'age' in data
def create_user(data: dict) -> str:
    """ Return a string 'User Created' if the dictionary contains 'name' and 'age'. 
    If not, return 'Invalid User Data'. The 'name' should be a non-empty string and 'age' 
    should be an integer greater than 0.

    >>> create_user({'name': 'John', 'age': 23})
    'User Created'
    >>> create_user({'name': 'John', 'height': 170})
    'Invalid User Data'
    >>> create_user({'name': '', 'age': 23})
    'Invalid User Data'
    >>> create_user({'name': 'John', 'age': -5})
    'Invalid User Data'
    """
    if validate_input(data):
        if isinstance(data['name'], str) and data['name'] != '' and isinstance(data['age'], int) and (data['age'] > 0):
            return 'User Created'
        else:
            return 'Invalid User Data'
    else:
        return 'Invalid User Data'