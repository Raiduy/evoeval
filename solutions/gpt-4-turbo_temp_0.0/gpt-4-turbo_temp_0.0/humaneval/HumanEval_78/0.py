
def hex_key(num):
    # Define a set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Initialize a counter for prime digits
    prime_count = 0
    
    # Iterate through each character in the input string
    for digit in num:
        # If the digit is a prime hexadecimal digit, increment the counter
        if digit in prime_hex_digits:
            prime_count += 1
            
    # Return the count of prime hexadecimal digits
    return prime_count
