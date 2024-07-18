from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    total_cost = 0.0
    for item in items:
        if isinstance(item, str):
            total_cost += 5.0
            if location in ['National', 'International']:
                total_cost += 10.0
        elif isinstance(item, float) and item > 5.0:
            total_cost += 5.0
            total_cost += 10.0
        else:
            total_cost += 5.0
    if location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    return round(total_cost, 2)