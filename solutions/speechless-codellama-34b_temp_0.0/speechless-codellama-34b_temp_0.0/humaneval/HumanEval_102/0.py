
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x and y are positive numbers
    if x <= 0 or y <= 0:
        return -1
    
    # Check if x is greater than y
    if x > y:
        return -1
    
    # Initialize the biggest even number to -1
    biggest_even = -1
    
    # Loop through the range [x, y] inclusive
    for i in range(x, y+1):
        # Check if the current number is even
        if i % 2 == 0:
            # Update the biggest even number if the current number is bigger
            biggest_even = max(biggest_even, i)
    
    # Return the biggest even number or -1 if there's no such number
    return biggest_even
