def recipe_converter(recipe, conversion_factor):
    converted_recipe = {}
    for (ingredient, quantity) in recipe.items():
        converted_recipe[ingredient] = quantity * conversion_factor
    return converted_recipe