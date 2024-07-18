

def fizz_buzz(n: int):
    """Returns count of digit '7' in numbers less than 'n' that are multiples of 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count