

def sort_third(l: list):
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three.sort()
    new_list = [divisible_by_three.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]
    return new_list