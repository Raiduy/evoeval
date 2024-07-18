
def simplify(x, n):
    (num1, den1) = map(int, x.split('/'))
    (num2, den2) = map(int, n.split('/'))
    result_num = num1 * num2
    result_den = den1 * den2
    if result_num % result_den == 0:
        return True
    else:
        return False