from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    base_cost = 5.0
    additional_cost = 10.0
    local_factor = 1.0
    national_factor = 1.5
    international_factor = 2.5
    total_weight = 0
    string_items = False
    for item in items:
        if isinstance(item, str):
            total_weight += 1
            string_items = True
        else:
            total_weight += item
    if total_weight > 5 and (not string_items):
        base_cost += additional_cost
    if location == 'Local':
        factor = local_factor
    elif location == 'National':
        factor = national_factor
    elif location == 'International':
        factor = international_factor
    else:
        factor = local_factor
    if string_items:
        factor *= 1.5
    total_cost = base_cost * total_weight * factor
    return round(total_cost, 2)