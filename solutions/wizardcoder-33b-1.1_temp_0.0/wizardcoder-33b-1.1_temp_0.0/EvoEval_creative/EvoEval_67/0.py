def meal_calculator(customers, meals):
    result = {}
    for customer in customers:
        if customer in meals:
            result[customer] = sum((meal['calories'] for meal in meals[customer]))
        else:
            result[customer] = 0
    return result