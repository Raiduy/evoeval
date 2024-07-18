
def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Sort the keys in descending order
    keys = sorted(freq.keys(), reverse=True)

    # Loop through the keys
    for key in keys:
        # Check if the key is greater than zero and has a frequency greater than or equal to the value of the integer itself
        if key > 0 and freq[key] >= key:
            return key

    # If no such a value exists, return -1
    return -1
