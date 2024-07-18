from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> str:
    total_weight = 0.0
    has_string = False
    for item in items:
        if isinstance(item, str):
            if not has_string:
                total_weight += 1.5
                has_string = True
        else:
            total_weight += item
    base_cost = len(items) * 5.0
    if total_weight > 5.0:
        base_cost += 10.0
    if location == 'Local':
        total_cost = base_cost
    elif location == 'National':
        total_cost = base_cost * 1.5
    elif location == 'International':
        total_cost = base_cost * 2.5
    else:
        total_cost = base_cost
    return '{:.2f}'.format(total_cost)