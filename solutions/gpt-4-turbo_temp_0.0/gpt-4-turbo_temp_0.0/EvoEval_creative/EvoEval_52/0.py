def magic_cookie_baker(n, m, orders):
    fulfillable_orders = 0
    for order in orders:
        if order == n:
            fulfillable_orders += 1
            if fulfillable_orders == m:
                break
    return min(fulfillable_orders, m)