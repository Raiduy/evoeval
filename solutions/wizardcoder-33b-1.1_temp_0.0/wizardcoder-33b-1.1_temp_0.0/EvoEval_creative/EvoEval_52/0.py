def magic_cookie_baker(n, m, orders):
    orders.sort()
    fulfilled_orders = 0
    for order in orders:
        if order <= n:
            n -= order
            fulfilled_orders += 1
        elif m > 1:
            m -= 1
            n = n
            n -= order
            fulfilled_orders += 1
        else:
            break
    return fulfilled_orders