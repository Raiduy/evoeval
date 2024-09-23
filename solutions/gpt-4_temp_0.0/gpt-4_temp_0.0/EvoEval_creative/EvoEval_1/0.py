from typing import List, Union

def calculate_shipping_cost(items: List[Union[str, float]], location: str) -> float:
    location_factor = {'Local': 1.0, 'National': 1.5, 'International': 2.5}
    total_cost = 0.0
    for item in items:
        if isinstance(item, str):
            weight = 1.0
        else:
            weight = item
        cost = 5.0
        if weight > 5.0:
            cost += 10.0
        total_cost += cost
    factor = location_factor.get(location, 1.0)
    total_cost *= factor
    return round(total_cost, 2)