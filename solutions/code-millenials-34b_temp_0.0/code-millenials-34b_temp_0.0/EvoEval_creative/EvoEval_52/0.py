def magic_cookie_baker(n, m, orders):
    orders.sort()
    fulfilled_orders = 0
    current_batch = 0
    for order in orders:
        if current_batch + order <= n:
            current_batch += order
        elif current_batch > 0:
            fulfilled_orders += 1
            current_batch = order
        else:
            continue
        if fulfilled_orders == m:
            break
    return fulfilled_orders