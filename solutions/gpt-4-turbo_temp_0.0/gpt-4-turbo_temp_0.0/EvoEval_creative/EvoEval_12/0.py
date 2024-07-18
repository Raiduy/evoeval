from typing import List

def teleporter_energy_signature(flux_values: List[int]) -> int:
    flux_counter = Counter(flux_values)
    most_occurred_element = sorted(flux_counter.most_common(), key=lambda x: (-x[1], x[0]))[-1][0]
    total_sum = sum(flux_values)
    energy_signature = total_sum * most_occurred_element
    return energy_signature