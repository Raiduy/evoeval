from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    base_cost = 5.0
    additional_charge = 10.0
    local_factor = 1.0
    national_factor = 1.5
    international_factor = 2.5
    total_weight = 0
    for item in items:
        if isinstance(item, str):
            total_weight += 1
        else:
            total_weight += item
    if total_weight > 5:
        base_cost += additional_charge
    if location == 'Local':
        factor = local_factor
    elif location == 'National':
        factor = national_factor
    elif location == 'International':
        factor = international_factor
    else:
        factor = local_factor
    total_cost = base_cost * len(items) * factor
    return round(total_cost, 2)