
def largest_smallest_integers(lst):
    negative_numbers = sorted([i for i in lst if i < 0], reverse=True)
    positive_numbers = sorted([i for i in lst if i > 0])
    a = negative_numbers[0] if negative_numbers else None
    b = positive_numbers[0] if positive_numbers else None
    return (a, b)