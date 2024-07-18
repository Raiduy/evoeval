def recipe_ingredients(recipe, available):
    for (ingredient, quantity) in recipe.items():
        if ingredient not in available or available[ingredient] < quantity:
            return False
    return True