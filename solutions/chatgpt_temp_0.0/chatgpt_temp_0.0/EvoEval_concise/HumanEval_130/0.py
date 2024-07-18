
def tri(n):
    """
    This function returns the first n+1 numbers of the Tribonacci sequence. 
    The Tribonacci sequence is defined as:
    - tri(1) = 3,
    - tri(n) = 1 + n / 2, if n is even,
    - tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    The function's input is a non-negative integer n.
     
    Example:
    tri(3) = [1, 3, 2, 8]
    """
    sequence = [3]
    if n == 0:
        return sequence
    for i in range(1, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i + 1])
    return sequence