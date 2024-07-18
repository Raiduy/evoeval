
def pluck(arr):
    # Initialize variables to store the smallest even value and its index
    smallest_even = float('inf')  # Use infinity as the initial value for comparison
    index_of_smallest_even = -1

    # Iterate through the array to find the smallest even value and its index
    for i, value in enumerate(arr):
        # Check if the current value is even and smaller than the current smallest_even
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            index_of_smallest_even = i

    # Check if an even value was found
    if index_of_smallest_even == -1:
        return []  # Return an empty list if no even value was found
    else:
        return [smallest_even, index_of_smallest_even]  # Return the smallest even value and its index
