
def largest_smallest_integers(lst):
    negative = []
    positive = []
    for i in lst:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
    return (None if not negative else max(negative), None if not positive else min(positive))
