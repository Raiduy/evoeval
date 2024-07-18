def magic_cookie_baker(n, m, orders):
    """
    You are a magical baker who bakes cookies with an enchanted oven.

    Your oven is special because it can bake exactly n cookies at once, and no more or less. Moreover, you can only bake m batches in a day. 

    Given a list of orders in the format of a list of positive integers where each integer represents an order for a specific number of cookies, return the maximum number of orders you can fulfill in a day.

    The function magic_cookie_baker should take three parameters: 
    - n (a positive integer) represents the exact number of cookies your oven can bake at once.
    - m (a positive integer) represents the maximum number of batches you can bake in a day.
    - orders (a list of positive integers) represents all the orders for the day.

    The function should assume that:
    - You can only bake one batch at a time.
    - You cannot split an order across multiple batches.
    - You cannot combine multiple orders into a single batch.

    The function should return an integer representing the maximum number of orders you can fulfill in a day.

    Example:
    assert magic_cookie_baker(3, 2, [4, 6, 8, 10]) == 0
    assert magic_cookie_baker(5, 3, [7, 9, 11, 13, 15]) == 0
    assert magic_cookie_baker(2, 4, [2, 4, 6, 8, 10]) == 1
    assert magic_cookie_baker(1, 1, [1, 2, 3, 4, 5]) == 1
    assert magic_cookie_baker(4, 2, [3, 5, 7, 9, 11]) == 1
    """
    orders.sort()
    fulfilled_orders = 0
    for order in orders:
        if order <= n:
            fulfilled_orders += 1
            n -= order
        else:
            n = m
        if fulfilled_orders == len(orders) or n == 0:
            break
    return fulfilled_orders