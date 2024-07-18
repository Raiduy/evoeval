
def get_max_even_positive(l: list):
    l = [i for i in l if i > 0 and i % 2 == 0]
    return max(l) if l else -1