def pluck_and_prod(arr):
    if not arr:
        return ([], None)
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return ([], None)
    smallest_even_value = min(even_values)
    smallest_even_index = arr.index(smallest_even_value)
    plucked_node = [smallest_even_value, smallest_even_index]
    remaining_nodes = [abs(num) for num in arr if num != smallest_even_value]
    product_of_signs = 1 if sum([1 for num in arr if num < 0]) % 2 == 0 else -1
    sum_of_remaining_nodes = sum(remaining_nodes) * product_of_signs
    return (plucked_node, sum_of_remaining_nodes)