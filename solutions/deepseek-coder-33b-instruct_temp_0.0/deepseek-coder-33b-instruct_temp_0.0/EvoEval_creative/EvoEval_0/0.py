from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    base_cost = 5.0
    additional_cost = 10.0
    total_weight = 0.0
    has_heavy_item = False
    has_string_item = False
    for item in items:
        if isinstance(item, str):
            if not has_string_item:
                base_cost *= 1.5
                has_string_item = True
            total_weight += 1.0
        else:
            total_weight += item
            if item > 5.0:
                has_heavy_item = True
    total_cost = base_cost * len(items)
    if has_heavy_item:
        total_cost += additional_cost
    if location == 'Local':
        pass
    elif location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    return '{:.2f}'.format(total_cost)