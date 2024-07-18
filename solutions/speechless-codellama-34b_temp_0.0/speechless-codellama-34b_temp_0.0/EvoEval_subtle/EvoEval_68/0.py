
def pluck(arr):
    odd_values = [value for (index, value) in enumerate(arr) if value % 2 != 0]
    if not odd_values:
        return []
    smallest_odd_value = min(odd_values)
    smallest_odd_index = arr.index(smallest_odd_value)
    return [smallest_odd_index, smallest_odd_value]