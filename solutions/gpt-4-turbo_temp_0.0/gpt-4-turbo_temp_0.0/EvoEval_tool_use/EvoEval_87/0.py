def parse_order(order):
    """
    Parse an order string and return a tuple (product_id, quantity).
    If the order is not in the correct format, return None.
    """
    parts = order.split()
    if len(parts) != 2:
        return None
    product_id, quantity_str = parts
    if not quantity_str.isdigit():
        return None
    quantity = int(quantity_str)
    return (product_id, quantity)
def process_orders(orders, product_ids):
    """
    You are given two lists: orders and product_ids. Each element in the 
    orders list is a string, representing an order, in the format "product_id quantity". 
    Each order represents a request for a certain quantity of a product.
    The product_ids list contains strings, each representing a valid product id.
    
    Your task is to process the orders. For each order, if the product_id exists in the 
    product_ids list and the quantity is a positive integer, add it to the final list. 
    Otherwise, ignore the order.
    
    Return a list of tuples, where each tuple represents a valid order and is in the 
    format (product_id, quantity). The orders should appear in the same order 
    as they appear in the original orders list.
    
    The function should not raise any exceptions if any of the input orders are invalid.
    Instead, it should simply ignore any invalid orders.
    """
    valid_orders = []
    for order in orders:
        parsed_order = parse_order(order)
        if parsed_order is not None:
            (product_id, quantity) = parsed_order
            if product_id in product_ids and quantity > 0:
                valid_orders.append((product_id, quantity))
    return valid_orders