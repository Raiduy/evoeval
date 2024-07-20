from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> str:
    base_cost = 5.0
    additional_charge = 10.0
    string_multiplier = 1.5
    location_factors = {'Local': 1.0, 'National': 1.5, 'International': 2.5}
    total_cost = 0.0
    string_present = False
    for item in items:
        if isinstance(item, str):
            total_cost += base_cost * string_multiplier
            string_present = True
        else:
            total_cost += base_cost
            if item > 5.0:
                total_cost += additional_charge
    location_factor = location_factors.get(location, 1.0)
    total_cost *= location_factor
    if string_present:
        total_cost *= string_multiplier
    return '{:.2f}'.format(total_cost)