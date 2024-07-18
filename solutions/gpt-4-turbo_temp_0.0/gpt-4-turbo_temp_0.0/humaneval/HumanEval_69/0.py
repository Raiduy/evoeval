
def search(lst):
    # Count the frequency of each integer
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Initialize the result variable
    result = -1
    # Iterate through the frequency dictionary
    for num, freq in frequency.items():
        # Check if the frequency is greater than or equal to the number itself
        if num <= freq:
            # Update the result if the current number is greater than the previous result
            result = max(result, num)
    
    return result
