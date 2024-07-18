
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    """
    # Define vowels for easy checking and their replacements
    vowels = 'aeiouAEIOU'
    # Mapping vowels to their replacements
    replacements = {'a': 'c', 'A': 'C', 'e': 'g', 'E': 'G', 'i': 'k', 'I': 'K', 'o': 'q', 'O': 'Q', 'u': 'w', 'U': 'W'}
    
    # Initialize an empty string to store the encoded message
    encoded_message = ''
    
    # Iterate through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Swap the case of the character
            swapped_case_char = char.swapcase()
            # Check if the character is a vowel
            if swapped_case_char in vowels:
                # Replace the vowel with the letter 2 places ahead in the alphabet
                encoded_message += replacements[swapped_case_char]
            else:
                # If it's not a vowel, just add the swapped case character to the encoded message
                encoded_message += swapped_case_char
        else:
            # If the character is not a letter, just add it to the encoded message
            encoded_message += char
    
    return encoded_message
