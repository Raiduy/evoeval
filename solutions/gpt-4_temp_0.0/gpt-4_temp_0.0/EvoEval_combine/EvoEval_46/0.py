
def get_max_even_positive(l):
    positive_even_numbers = [num for num in l if num > 0 and num % 2 == 0]
    if not positive_even_numbers:
        return -1
    return max(positive_even_numbers)