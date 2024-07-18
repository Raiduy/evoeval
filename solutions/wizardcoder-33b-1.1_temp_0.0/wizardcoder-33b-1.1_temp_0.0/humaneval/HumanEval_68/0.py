
def pluck(arr):
    even_values = [(value, index) for index, value in enumerate(arr) if value % 2 == 0]
    if not even_values:
        return []
    else:
        return min(even_values, key=lambda x: (x[0], x[1]))
