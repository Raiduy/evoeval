
def pluck(arr):
    odd_values = [(i, val) for (i, val) in enumerate(arr) if val % 2 == 1]
    if not odd_values:
        return []
    else:
        return min(odd_values, key=lambda x: (x[1], x[0]))