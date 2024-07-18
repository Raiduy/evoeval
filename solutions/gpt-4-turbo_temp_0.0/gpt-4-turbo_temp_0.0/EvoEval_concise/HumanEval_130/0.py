
def tri(n):
    """
    This function returns the first n numbers of the Tribonacci sequence. 
    The Tribonacci sequence is defined as follows:
    - tri(0) = 0,
    - tri(1) = 1,
    - tri(2) = 1,
    - tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3) for n > 2.
    The function's input is a non-negative integer n.
     
    Example:
    tri(4) = [0, 1, 1, 2, 4]
    """
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]
    sequence = [0, 1, 1]
    for i in range(3, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_value)
    return sequence