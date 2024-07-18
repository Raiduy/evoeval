
def get_max_even_positive(l: list):
    even_positives = [num for num in l if num > 0 and num % 2 == 0]
    if not even_positives:
        return -1
    return max(even_positives)