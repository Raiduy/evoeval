
def generate_integers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    even_integers = [i for i in range(lower, upper + 1) if i % 2 == 0]
    return even_integers