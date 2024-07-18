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

def process_stock_data(data: List[Dict[str, str]], valid_symbols: List[str]) -> List[Dict[str, str]]:
    """Process the stock data and remove invalid entries

    Valid entries consist of valid symbols, accompanied by positive float prices.

    >>> process_stock_data([], [])
    []
    >>> process_stock_data([{'symbol': 'AAPL', 'price': '150.25'}, {'symbol': 'MSFT', 'price': '0.00'}], ["AAPL", "GOOGL", "TSLA", "AMZN", "FB"])
    [{'symbol': 'AAPL', 'price': '150.25'}]
    """
    valid_data = []
    for entry in data:
        if entry['symbol'] in valid_symbols and is_valid_price(entry['price']):
            valid_data.append(entry)
    return valid_data