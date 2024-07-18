
def get_closest_vowel(word):
    """Find the closest vowel that stands between two consonants from the right side of the word."""
    vowels = "aeiouAEIOU"
    # Reverse the word to start checking from the right
    reversed_word = word[::-1]
    
    # Iterate through the reversed word to find the first vowel that meets the condition
    for i in range(1, len(reversed_word) - 1):
        if (reversed_word[i] in vowels and 
            reversed_word[i-1] not in vowels and 
            reversed_word[i+1] not in vowels):
            # Return the found vowel
            return reversed_word[i]
    
    # Return an empty string if no vowel meets the condition
    return ""
