from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    BASE_COST = 5.0
    ADDITIONAL_COST = 10.0
    total_cost = 0.0
    for item in items:
        if isinstance(item, str):
            weight = 1.0
        else:
            weight = item
        total_cost += BASE_COST
        if weight > 5.0:
            total_cost += ADDITIONAL_COST
    if location == 'Local':
        pass
    elif location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    return round(total_cost, 2)