def cooking_challenge(ingredient_dict):
    if not ingredient_dict:
        return []
    ingredient_list = list(ingredient_dict.items())
    sorted_ingredients = sorted(ingredient_list, key=lambda x: (-x[1], x[0]))
    return sorted_ingredients