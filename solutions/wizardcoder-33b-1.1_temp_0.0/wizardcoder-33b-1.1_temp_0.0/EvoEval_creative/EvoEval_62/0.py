def recipe_converter(recipe, conversion_factor):
    return {ingredient: quantity * conversion_factor for (ingredient, quantity) in recipe.items()}