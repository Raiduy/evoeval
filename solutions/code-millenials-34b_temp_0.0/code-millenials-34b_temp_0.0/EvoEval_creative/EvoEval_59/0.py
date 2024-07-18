def cooking_challenge(ingredient_dict):
    sorted_dict = sorted(ingredient_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_dict