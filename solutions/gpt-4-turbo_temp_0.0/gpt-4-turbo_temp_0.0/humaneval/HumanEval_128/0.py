
def prod_signs(arr):
    if not arr:  # Check if the array is empty
        return None
    
    sign_product = 1  # Initialize the product of signs as 1 (neutral element for multiplication)
    magnitude_sum = 0  # Initialize the sum of magnitudes
    
    for num in arr:
        if num > 0:
            sign_product *= 1  # Positive number, multiply by 1
        elif num < 0:
            sign_product *= -1  # Negative number, multiply by -1
        else:
            sign_product *= 0  # Zero found, product of signs will be 0
            break  # No need to continue, the result will be 0
        
        magnitude_sum += abs(num)  # Add the absolute value of the number to the magnitude sum
    
    return sign_product * magnitude_sum
