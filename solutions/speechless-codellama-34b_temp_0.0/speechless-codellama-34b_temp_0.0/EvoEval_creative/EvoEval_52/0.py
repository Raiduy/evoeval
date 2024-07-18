def magic_cookie_baker(n, m, orders):
    orders.sort(reverse=True)
    count = 0
    for order in orders:
        if order <= n * m:
            count += 1
            m -= 1
        else:
            break
    return count