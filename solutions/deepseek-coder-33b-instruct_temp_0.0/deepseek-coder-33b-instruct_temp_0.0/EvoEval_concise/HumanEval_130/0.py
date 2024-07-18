
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
    if n == 1:
        return [3]
    elif n % 2 == 0:
        return [1 + n / 2]
    else:
        return [tri(n - 1) + tri(n - 2) + tri(n + 1)]