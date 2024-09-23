def recipe_ingredients(recipe, available):
    """Checks if a particular recipe can be cooked with the available ingredients.

    Args:
        recipe (dict): A dictionary where the keys are the ingredient names and the values are the quantities.
        available (dict): A dictionary where the keys are the ingredient names and the values are the quantities.

    Returns:
        bool: True if all ingredients needed for the recipe are available, False otherwise.
    """
    for (ingredient, quantity) in recipe.items():
        if ingredient not in available or available[ingredient] < quantity:
            return False
    return True