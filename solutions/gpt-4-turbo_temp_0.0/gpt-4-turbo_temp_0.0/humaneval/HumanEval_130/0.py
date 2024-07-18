
def tri(n):
    """Return the first n + 1 numbers of a modified Tribonacci sequence.
    The sequence starts with 1, 3, 2 and each subsequent number is the sum of the preceding three.
    """
    # Base cases for the first three numbers in the sequence
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    
    # Initialize the sequence with the first three numbers
    sequence = [1, 3, 2]
    
    # Calculate the rest of the sequence up to n
    for i in range(3, n + 1):
        next_value = sequence[i-1] + sequence[i-2] + sequence[i-3]
        sequence.append(next_value)
    
    return sequence
