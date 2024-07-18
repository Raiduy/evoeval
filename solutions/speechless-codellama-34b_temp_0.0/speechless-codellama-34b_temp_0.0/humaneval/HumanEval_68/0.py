
def pluck(arr):
    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []
    smallest_even_node = min(even_nodes)
    smallest_even_node_index = arr.index(smallest_even_node)
    return [smallest_even_node, smallest_even_node_index]
