def recipe_converter(recipe, conversion_factor):
    new_recipe = {}
    for (ingredient, quantity) in recipe.items():
        new_recipe[ingredient] = quantity * conversion_factor
    return new_recipe