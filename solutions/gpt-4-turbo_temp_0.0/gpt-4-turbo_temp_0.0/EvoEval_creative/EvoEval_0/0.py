from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> str:
    base_cost_per_item = 5.0
    total_cost = 0.0
    string_item_multiplier = 1.0
    location_multiplier = 1.0
    if any((isinstance(item, str) for item in items)):
        string_item_multiplier = 1.5
    if location == 'Local':
        location_multiplier = 1.0
    elif location == 'National':
        location_multiplier = 1.5
    elif location == 'International':
        location_multiplier = 2.5
    for item in items:
        if isinstance(item, str):
            item_weight = 1.0
        else:
            item_weight = item
        item_cost = base_cost_per_item
        if item_weight > 5:
            item_cost += 10.0
        total_cost += item_cost
    total_cost *= string_item_multiplier * location_multiplier
    return f'{total_cost:.2f}'