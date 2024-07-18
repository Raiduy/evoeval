def cooking_challenge(ingredient_dict):
    if not ingredient_dict:
        return []
    sorted_ingredients = sorted(ingredient_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_ingredients