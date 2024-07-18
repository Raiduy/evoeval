
def get_max_even_positive(l: list):
    even_positive_numbers = [num for num in l if num > 0 and num % 2 == 0]
    if not even_positive_numbers:
        return -1
    return max(even_positive_numbers)