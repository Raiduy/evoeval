def cooking_challenge(ingredient_dict):
    """
    Given a dictionary where the keys are the main ingredients and the values are the number of recipes you can cook with this ingredient,
    return a list of tuples where the first element of each tuple is an ingredient and the second is a number of recipes. The list should be 
    sorted in descending order based on the number of recipes. If two ingredients can be used in the same number of recipes, sort them in ascending 
    alphabetical order.
    The function should return an empty list if the given dictionary is empty.
    
    Examples:
    cooking_challenge({"Chicken": 5, "Beef": 10, "Fish": 2}) should return [('Beef', 10), ('Chicken', 5), ('Fish', 2)].
    cooking_challenge({"Tomato": 10, "Potato": 10, "Onion": 5}) should return [('Potato', 10), ('Tomato', 10), ('Onion', 5)].
    cooking_challenge({"Eggs": 3, "Milk": 0, "Flour": 2}) should return [('Eggs', 3), ('Flour', 2), ('Milk', 0)].
    cooking_challenge({}) should return [].
    """
    if not ingredient_dict:
        return []
    else:
        sorted_ingredients = sorted(ingredient_dict.items(), key=lambda x: (-x[1], x[0]))
        return sorted_ingredients