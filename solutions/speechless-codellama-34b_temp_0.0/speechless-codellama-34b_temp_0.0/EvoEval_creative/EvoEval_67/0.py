def meal_calculator(customers, meals):
    result = {}
    for customer in customers:
        if customer in meals:
            total_calories = 0
            for meal in meals[customer]:
                total_calories += meal['calories']
            result[customer] = total_calories
        else:
            result[customer] = 0
    return result