def meal_calculator(customers, meals):
    result = {}
    for customer in customers:
        if customer in meals:
            total_calories = sum((meal['calories'] for meal in meals[customer]))
            result[customer] = total_calories
        else:
            result[customer] = 0
    return result