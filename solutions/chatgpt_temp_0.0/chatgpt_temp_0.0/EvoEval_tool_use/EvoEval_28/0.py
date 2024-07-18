def is_valid_price(price: str) -> bool:
    """Check if a price is valid or not
    :param price: the price of the stock
    :return: True if valid, False otherwise
    """
    if price.replace(".", "", 1).isdigit() and float(price) > 0:
        return True
    else:
        return False
from typing import List, Dict

