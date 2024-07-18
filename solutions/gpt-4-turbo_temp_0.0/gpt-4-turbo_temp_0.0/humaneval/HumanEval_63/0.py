

def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence."""
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store computed values
    fibfib_values = [0] * (n+1)
    fibfib_values[0], fibfib_values[1], fibfib_values[2] = 0, 0, 1
    
    # Compute fibfib values from 3 to n
    for i in range(3, n+1):
        fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
    
    return fibfib_values[n]
