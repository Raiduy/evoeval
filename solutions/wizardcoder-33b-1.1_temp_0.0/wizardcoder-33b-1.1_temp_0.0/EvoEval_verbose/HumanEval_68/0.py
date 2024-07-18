
def pluck(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    if not even_numbers:
        return []
    smallest_even_number = min(even_numbers)
    index_of_smallest_even_number = arr.index(smallest_even_number)
    return [smallest_even_number, index_of_smallest_even_number]