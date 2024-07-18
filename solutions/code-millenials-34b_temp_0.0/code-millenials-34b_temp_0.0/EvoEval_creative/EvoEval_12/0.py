from typing import List

def teleporter_energy_signature(flux_values: List[int]) -> int:
    max_count = max(Counter(flux_values).values())
    most_occurred = min([num for (num, freq) in Counter(flux_values).items() if freq == max_count])
    total_sum = sum(flux_values)
    return total_sum * most_occurred