def potion_mixing(potions, target):
    potion_dict = {}
    for potion in potions:
        (name, power) = potion.split()
        potion_dict[name] = int(power)
    combinations = []
    for (name, power) in potion_dict.items():
        if power == target:
            combinations.append([name])
            continue
        if power < target:
            for (other_name, other_power) in potion_dict.items():
                if name != other_name:
                    if power + other_power == target:
                        combinations.append([name, other_name])
                        continue
    combinations.sort(key=lambda x: (len(x), ''.join(x)))
    if combinations:
        return combinations[0]
    else:
        return []