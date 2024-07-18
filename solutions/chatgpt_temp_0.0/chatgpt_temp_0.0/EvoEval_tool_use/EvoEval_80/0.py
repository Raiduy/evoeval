def read_items(items_str):
    """Converts the string representation of a list of items into a Python list.
    
    The string representation of a list follows the format:
    '{first_item,second_item,third_item,...,last_item}'
    """
    items_str = items_str.strip('{}')
    return items_str.split(',')


def validate_item(items):
    """Validates the items of a Python list.
    
    Each valid item is a string of digits that represents a positive integer.
    An item is invalid if it consists of non-digit characters or if it represents a non-positive integer.
    This function checks each item in the list and removes invalid items.
    """
    return [item for item in items if item.isdigit() and int(item) > 0]
def add_items(items_str):
    """
    This function takes a string representation of a list of items and returns their sum.
    Each item is separated by a ','. 

    The string starts and ends with a '{' and '}' respectively.
    If input does not follow the format, return "Invalid"

    For each item, if it's not a positive integer, ignore it.

    Finally, return the sum of all the individual digits in the valid items. If no valid items found, return 0.

    Examples:
    add_items('{1,2,3,4,5}')  # returns 15
    add_items('{a,b,3,d,e}')  # returns 3
    add_items('{10,a,20,b,30}')  # returns 6
    add_items('{}')  # returns 0
    """
    items = read_items(items_str)
    valid_items = validate_item(items)
    if len(items) != len(valid_items):
        return 'Invalid'
    return sum((int(item) for item in valid_items))