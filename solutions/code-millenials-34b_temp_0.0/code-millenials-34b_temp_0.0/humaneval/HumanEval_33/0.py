

def sort_third(l: list):
    divisible_by_three = sorted([l[i] for i in range(len(l)) if (i + 1) % 3 == 0])
    result = [divisible_by_three.pop(0) if (i + 1) % 3 == 0 else l[i] for i in range(len(l))]
    return result
