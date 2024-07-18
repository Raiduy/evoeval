
def get_odd_collatz(n):
    """
    Given a positive integer n, this function returns a sorted list of the odd numbers in the Collatz sequence.
    
    Collatz sequence starts with a positive integer n. Each subsequent term is derived from the previous term: 
    - If the previous term is even, the next term is half of the previous term.
    - If the previous term is odd, the next term is 3 times the previous term plus 1.
    The sequence always concludes at 1, regardless of the initial n.

    Note: 
        1. Collatz(1) returns [1].
        2. The returned list is sorted in ascending order.

    Example:
    get_odd_collatz(5) returns [1, 5] # The Collatz sequence for 5 is [5, 16, 8, 4, 2, 1], hence the odd numbers are 1 and 5.
    """
    collatz_sequence = []
    while n != 1:
        collatz_sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    collatz_sequence.append(1)
    odd_collatz_sequence = sorted([num for num in collatz_sequence if num % 2 != 0])
    return odd_collatz_sequence