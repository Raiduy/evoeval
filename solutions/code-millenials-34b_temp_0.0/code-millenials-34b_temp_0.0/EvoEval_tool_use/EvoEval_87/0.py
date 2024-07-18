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
    Process the orders and return a list of tuples, where each tuple represents a valid order.
    """
    processed_orders = []
    for order in orders:
        parsed_order = parse_order(order)
        if parsed_order is not None and parsed_order[0] in product_ids and (parsed_order[1] > 0):
            processed_orders.append(parsed_order)
    return processed_orders