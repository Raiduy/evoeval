
def largest_smallest_integers(lst):
    negative_nums = [i for i in lst if i < 0]
    positive_nums = [i for i in lst if i > 0]
    if not negative_nums and (not positive_nums):
        return (None, None)
    elif not negative_nums:
        return (None, min(positive_nums))
    elif not positive_nums:
        return (max(negative_nums), None)
    else:
        return (max(negative_nums), min(positive_nums))