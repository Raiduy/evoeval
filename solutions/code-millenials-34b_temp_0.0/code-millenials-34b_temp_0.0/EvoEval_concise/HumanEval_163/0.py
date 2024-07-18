
def generate_integers(a, b):
    if a > b:
        (a, b) = (b, a)
    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers