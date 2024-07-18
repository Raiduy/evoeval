
def generate_integers(a, b):
    # Swap a and b if a > b
    if a > b:
        a, b = b, a

    # Initialize the result list
    result = []

    # Loop through the range from a to b
    for i in range(a, b + 1):
        # Check if the number is even
        if i % 2 == 0:
            # Convert the number to a string and loop through its digits
            for digit in str(i):
                # If the digit is even, add it to the result list
                if int(digit) % 2 == 0:
                    result.append(int(digit))
    
    # Remove duplicates and sort the result list
    result = sorted(list(set(result)))

    return result
