
def pluck(arr):
    even_nodes = [(i, val) for (i, val) in enumerate(arr) if val % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: (x[1], x[0]))
    else:
        return []