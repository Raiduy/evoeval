
def generate_integers(a, b):
    result = []
    for i in range(min(a, b), max(a, b)+1):
        if i % 2 == 0:
            result.append(i)
    return result
