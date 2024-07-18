def pluck_and_prod(arr):
    if not arr:
        return ([], None)
    smallest_even_index = -1
    smallest_even_value = float('inf')
    for (i, num) in enumerate(arr):
        if num % 2 == 0 and num < smallest_even_value:
            smallest_even_index = i
            smallest_even_value = num
    if smallest_even_index == -1:
        return ([], None)
    else:
        plucked_node = [arr[smallest_even_index], smallest_even_index]
        remaining_nodes = arr[:smallest_even_index] + arr[smallest_even_index + 1:]
        remaining_sum = sum([abs(num) * (1 if num > 0 else -1 if num < 0 else 0) for num in remaining_nodes])
        return (plucked_node, remaining_sum)