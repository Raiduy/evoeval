
def select_words(s, n):
    # Define a list to hold the words that match the criteria
    matching_words = []
    
    # Define a set of consonants for easy checking
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    # Split the string into words
    words = s.split()
    
    # Iterate through each word
    for word in words:
        # Count the consonants in the current word
        consonant_count = sum(1 for char in word if char in consonants)
        
        # If the count matches n, add the word to the list
        if consonant_count == n:
            matching_words.append(word)
    
    # Return the list of matching words
    return matching_words
