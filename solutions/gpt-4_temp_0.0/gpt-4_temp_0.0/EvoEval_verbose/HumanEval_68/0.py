
def pluck(arr):
    if not arr:
        return []
    else:
        even_values = [(val, idx) for (idx, val) in enumerate(arr) if val % 2 == 0]
        if not even_values:
            return []
        else:
            return min(even_values)