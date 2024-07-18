def potion_mixing(potions, target):
    potions_with_power = [(potion, int(potion.split()[-1])) for potion in potions]
    potions_with_power.sort(key=lambda x: x[0])

    def find_combinations(index, current_sum, current_combination):
        if current_sum == target:
            return [current_combination]
        if current_sum > target or index == len(potions_with_power):
            return None
        combinations = []
        include_current = find_combinations(index + 1, current_sum + potions_with_power[index][1], current_combination + [potions_with_power[index][0]])
        if include_current:
            combinations.extend(include_current)
        exclude_current = find_combinations(index + 1, current_sum, current_combination)
        if exclude_current:
            combinations.extend(exclude_current)
        return combinations
    all_combinations = find_combinations(0, 0, [])
    if not all_combinations:
        return []
    best_combination = min(all_combinations, key=lambda x: (len(x), x))
    return best_combination