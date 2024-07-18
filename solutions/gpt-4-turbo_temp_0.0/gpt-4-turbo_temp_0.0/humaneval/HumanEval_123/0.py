
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
    """
    # Initialize an empty list to store the odd numbers
    odd_numbers = []
    
    # Continue the loop until n becomes 1
    while n != 1:
        # Check if the current number is odd
        if n % 2 != 0:
            # If it's odd, add it to the list
            odd_numbers.append(n)
        # Apply the Collatz rules
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    # After the loop, add 1 to the list since the sequence always ends with 1
    odd_numbers.append(1)
    
    # Return the sorted list of odd numbers
    return sorted(odd_numbers)
