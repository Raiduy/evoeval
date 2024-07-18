
def histogram(test):
    # Create a dictionary to store the frequency of each letter
    freq_dict = {}
    
    # Split the string into a list of letters
    letters = test.split()
    
    # Iterate over each letter in the list
    for letter in letters:
        # If the letter is already in the dictionary, increment its count
        if letter in freq_dict:
            freq_dict[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            freq_dict[letter] = 1

    # Find the maximum count
    max_count = max(freq_dict.values()) if freq_dict else 0

    # Create a new dictionary to store the letters with maximum count
    result = {}

    # Iterate over the letters and their counts in the original dictionary
    for letter, count in freq_dict.items():
        # If the count equals the maximum count, add the letter to the new dictionary
        if count == max_count:
            result[letter] = count

    return result
