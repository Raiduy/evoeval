def recipe_converter(recipe, conversion_factor):
    """
    Write a function that takes a dictionary representing a recipe as input 
    where the keys are the ingredients and the values are the quantities 
    needed for one serving. The function should also take a conversion factor 
    which represents the number of servings required. The function should 
    return a new dictionary where the quantities of each ingredient are 
    multiplied by the conversion factor.

    The quantities in the recipe are integers and the conversion factor is a 
    positive integer. 

    Examples:
    >>> recipe_converter({"flour": 500, "sugar": 200, "eggs": 3}, 2)
    {'flour': 1000, 'sugar': 400, 'eggs': 6}
    >>> recipe_converter({"milk": 250, "chocolate": 75, "butter": 50}, 3)
    {'milk': 750, 'chocolate': 225, 'butter': 150}
    """
    return {ingredient: quantity * conversion_factor for (ingredient, quantity) in recipe.items()}