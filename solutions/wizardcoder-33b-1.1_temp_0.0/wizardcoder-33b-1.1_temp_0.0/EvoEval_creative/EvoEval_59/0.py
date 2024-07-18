def cooking_challenge(ingredient_dict):
    if not ingredient_dict:
        return []
    else:
        ingredient_list = list(ingredient_dict.items())
        ingredient_list.sort(key=lambda x: (-x[1], x[0]))
        return ingredient_list