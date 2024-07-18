
def histogram(test):
    # Split the input string into a list of letters
    letters = test.split()
    
    # Create a dictionary to store the count of each letter
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    # Find the maximum count of occurrences
    max_count = max(letter_count.values(), default=0)
    
    # Create a dictionary to store letters with the maximum count
    max_letters = {letter: count for letter, count in letter_count.items() if count == max_count}
    
    return max_letters
