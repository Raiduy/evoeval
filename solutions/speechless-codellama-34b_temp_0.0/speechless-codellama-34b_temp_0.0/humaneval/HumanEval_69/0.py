
def search(lst):
    # Create an empty dictionary to store the frequency of each integer
    freq = {}
    
    # Iterate through the list and update the frequency of each integer
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Iterate through the dictionary and find the greatest integer that satisfies the condition
    max_val = -1
    for num, count in freq.items():
        if count >= num and num > max_val:
            max_val = num
    
    return max_val
