
def pluck(arr):
    even_nodes = [(val, idx) for (idx, val) in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    else:
        return min(even_nodes, key=lambda x: (x[0], x[1]))