def recipe_ingredients(recipe, available):
    """Checks if a particular recipe can be cooked with the available ingredients.

    Args:
        recipe (dict): A dictionary where the keys are the ingredient names and the values are the quantities.
        available (dict): A dictionary where the keys are the ingredient names and the values are the quantities.

    Returns:
        bool: True if all ingredients needed for the recipe are available, False otherwise.

    Examples:
        assert recipe_ingredients({'flour': 200, 'sugar': 100, 'eggs': 2}, {'flour': 500, 'sugar': 100, 'eggs': 2}) == True
        assert recipe_ingredients({'flour': 200, 'sugar': 100, 'eggs': 2}, {'flour': 100, 'sugar': 50, 'eggs': 1}) == False
        assert recipe_ingredients({'flour': 200, 'sugar': 100, 'milk': 100}, {'flour': 500, 'sugar': 100, 'eggs': 2}) == False
        assert recipe_ingredients({}, {'flour': 500, 'sugar': 100, 'eggs': 2}) == True
    """
    for (ingredient, quantity) in recipe.items():
        if ingredient not in available or available[ingredient] < quantity:
            return False
    return True