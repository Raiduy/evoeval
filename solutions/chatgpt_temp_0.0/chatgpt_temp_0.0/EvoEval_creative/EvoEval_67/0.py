def meal_calculator(customers, meals):
    """
    Write a function meal_calculator which takes two arguments; a list of customer's names and a dictionary representing meals consumed by customers where the key is the customer's name and the value is a list of meals. Each meal is a dictionary with a 'dish' and 'calories' key. The function should return a dictionary where each key is a customer's name and the value is the total calories consumed by that customer.

    If a customer's name does not exist in the meals dictionary, assume that the customer consumed 0 calories. The calories value for each meal will always be a positive integer.

    Example:
    >>> meal_calculator(['Alice', 'Bob', 'Charlie'], 
                        {'Alice': [{'dish':'Pizza', 'calories': 300}, {'dish':'Burger', 'calories': 500}], 
                         'Bob': [{'dish':'Salad', 'calories': 100}], 
                         'Charlie': [{'dish':'Fries', 'calories': 200}, {'dish':'Burger', 'calories': 500}, {'dish':'Ice Cream', 'calories': 250}]})
    {'Alice': 800, 'Bob': 100, 'Charlie': 950}

    >>> meal_calculator(['Tom', 'Jerry'], 
                        {'Tom': [{'dish':'Pizza', 'calories': 300}, {'dish':'Burger', 'calories': 500}], 
                         'Jerry': [{'dish':'Fries', 'calories': 200}]})
    {'Tom': 800, 'Jerry': 200}
    """
    total_calories = {}
    for customer in customers:
        if customer in meals:
            total_calories[customer] = sum([meal['calories'] for meal in meals[customer]])
        else:
            total_calories[customer] = 0
    return total_calories