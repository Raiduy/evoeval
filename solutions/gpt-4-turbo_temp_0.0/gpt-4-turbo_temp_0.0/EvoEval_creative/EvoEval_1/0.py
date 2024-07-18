from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    """
    Given a list of items (represented by their weights in kg) and a location,
    calculate the cost of shipping. Each item has a base shipping cost of $5.0.
    The location multiplies the total cost by a certain factor:
    - "Local": no additional factor
    - "National": factor of 1.5
    - "International": factor of 2.5
    - other location: no additional factor
    If the item's weight is more than 5kg, an additional charge of $10.0 is added.
    
    If an item is passed as a string instead of a float, consider its weight as 1kg.
    
    Return the total shipping cost rounded to two decimal places.
    """
    total_cost = 0.0
    for item in items:
        weight = 1.0 if isinstance(item, str) else item
        item_cost = 5.0
        if weight > 5:
            item_cost += 10.0
        total_cost += item_cost
    if location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    return round(total_cost, 2)