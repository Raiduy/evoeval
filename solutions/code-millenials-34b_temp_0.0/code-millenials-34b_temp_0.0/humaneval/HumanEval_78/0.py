
def hex_key(num):
    # Define the prime hexadecimal digits
    prime_hexes = set('2357BD')

    # Initialize a count variable
    count = 0

    # Go through the individual characters in the input string
    for char in num:
        # If the character is a prime hex, increment the count
        if char in prime_hexes:
            count += 1

    # Return the count
    return count
