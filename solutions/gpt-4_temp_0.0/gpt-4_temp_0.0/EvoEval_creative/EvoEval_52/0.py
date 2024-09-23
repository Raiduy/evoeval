def magic_cookie_baker(n, m, orders):
    orders.sort()
    count = 0
    for order in orders:
        if order <= n and count < m:
            count += 1
        else:
            break
    return count