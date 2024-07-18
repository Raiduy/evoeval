
def pluck(arr):
    if not arr:
        return []
    even_nodes = [(i, x) for (i, x) in enumerate(arr) if x % 2 == 0]
    if not even_nodes:
        return []
    smallest_even_node = min(even_nodes, key=lambda x: (x[1], x[0]))
    return [smallest_even_node[1], smallest_even_node[0]]