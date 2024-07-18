
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Initialize a counter for the number of even numbers found
    even_count = 0
    # Initialize a variable to store the sum of even numbers
    even_sum = 0
    # Iterate through all numbers from 2 to n
    for i in range(2, n+1):
        # Check if the current number is even
        if i % 2 == 0:
            # If it is even, increment the even count and add the number to the even sum
            even_count += 1
            even_sum += i
            # If the even count is greater than 4, return False
            if even_count > 4:
                return False
            # If the even sum is equal to n, return True
            if even_sum == n:
                return True
    # If no combination of 4 even numbers is found, return False
    return False
