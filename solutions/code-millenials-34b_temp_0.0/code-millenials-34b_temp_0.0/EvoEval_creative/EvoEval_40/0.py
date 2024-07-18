def potion_mixing(potions, target):
    potions.sort(key=lambda x: (int(x.split()[-1]), x))
    for i in range(len(potions)):
        for j in range(i + 1, len(potions)):
            if int(potions[i].split()[-1]) + int(potions[j].split()[-1]) == target:
                return [potions[i], potions[j]]
            elif int(potions[i].split()[-1]) + int(potions[j].split()[-1]) > target:
                break
    return []