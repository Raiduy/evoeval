def parse_items(items_str: str):
    """Parses a string of comma-separated items into a list.

    Args:
        items_str (str): A string of comma-separated items.

    Returns:
        list: A list of items.
    """
    return items_str.split(',')

def check_availability(item: str, available_items: list):
    """Checks if an item is available in the provided list.

    Args:
        item (str): The item to check.
        available_items (list): The list of available items.

    Returns:
        bool: True if the item is available, False otherwise.
    """
    return item in available_items
def place_order(order_str: str, available_items_str: str):
    """Places an order by checking the availability of each item in the order.

    If all items in the order are available, the function returns True, indicating that the order was successfully placed. If not, the function returns False.

    >>> place_order('apple,banana', 'apple,banana,orange')
    True
    >>> place_order('apple,banana,grape', 'apple,banana,orange')
    False
    """
    order = parse_items(order_str)
    available_items = parse_items(available_items_str)
    for item in order:
        if not check_availability(item, available_items):
            return False
    return True