from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    total_cost = 0.0
    additional_charge = 0.0
    weight_multiplier = 1.0
    for item in items:
        if isinstance(item, str):
            weight_multiplier *= 1.5
        else:
            total_cost += 5.0
            if item > 5.0:
                additional_charge += 10.0
    total_cost += additional_charge
    if location == 'Local':
        pass
    elif location == 'National':
        total_cost *= 1.5
    elif location == 'International':
        total_cost *= 2.5
    else:
        weight_multiplier *= 1.5
    total_cost *= weight_multiplier
    return round(total_cost, 2)