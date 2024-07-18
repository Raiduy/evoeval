
def get_max_even_positive(l: list):
    positive_evens = [num for num in l if num > 0 and num % 2 == 0]
    if not positive_evens:
        return -1
    return max(positive_evens)