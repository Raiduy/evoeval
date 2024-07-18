
def largest_smallest_integers(lst):
    negatives = [num for num in lst if num < 0]
    positives = [num for num in lst if num > 0]
    max_negative = None
    min_positive = None
    if negatives:
        max_negative = max(negatives)
    if positives:
        min_positive = min(positives)
    return (max_negative, min_positive)