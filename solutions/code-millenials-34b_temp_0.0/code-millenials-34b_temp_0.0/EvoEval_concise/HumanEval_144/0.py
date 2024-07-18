def simplify(x, n):
    (x_num, x_den) = map(int, x.split('/'))
    (n_num, n_den) = map(int, n.split('/'))
    new_num = x_num * n_num
    new_den = x_den * n_den
    return new_num % new_den == 0