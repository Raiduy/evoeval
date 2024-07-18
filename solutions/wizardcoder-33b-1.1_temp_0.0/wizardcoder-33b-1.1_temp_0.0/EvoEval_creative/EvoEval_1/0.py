from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    total_cost = 0
    for item in items:
        if isinstance(item, str):
            weight = 1
        else:
            weight = item
        if weight > 5:
            total_cost += 15
        else:
            total_cost += 5
    if location == 'Local':
        total_cost *= 1
    elif location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    else:
        total_cost *= 1
    return round(total_cost, 2)