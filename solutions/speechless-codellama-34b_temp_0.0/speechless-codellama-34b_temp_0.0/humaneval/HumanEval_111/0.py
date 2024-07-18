
def histogram(test):
    # Create an empty dictionary to store the frequency of each letter
    freq = {}
    
    # Split the input string into a list of letters
    letters = test.split()
    
    # Iterate over each letter in the list
    for letter in letters:
        # If the letter is already in the frequency dictionary, increment its count
        if letter in freq:
            freq[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            freq[letter] = 1
    
    # Find the maximum frequency
    max_freq = max(freq.values())
    
    # Create an empty dictionary to store the letters with the maximum frequency
    max_freq_letters = {}
    
    # Iterate over each letter in the frequency dictionary
    for letter, count in freq.items():
        # If the letter's count is equal to the maximum frequency, add it to the max_freq_letters dictionary
        if count == max_freq:
            max_freq_letters[letter] = count
    
    # Return the max_freq_letters dictionary
    return max_freq_letters
