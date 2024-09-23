def potion_mixing(potions, target):
    potions_with_power = [(potion, int(potion.split()[-1])) for potion in potions]
    possible_combinations = []
    for r in range(1, len(potions_with_power) + 1):
        for combination in itertools.combinations(potions_with_power, r):
            if sum((power for (_, power) in combination)) == target:
                possible_combinations.append(combination)
    if not possible_combinations:
        return []
    min_length = min((len(combination) for combination in possible_combinations))
    possible_combinations = [combination for combination in possible_combinations if len(combination) == min_length]
    possible_combinations.sort(key=lambda combination: ''.join((potion for (potion, _) in combination)))
    return [potion for (potion, _) in possible_combinations[0]]