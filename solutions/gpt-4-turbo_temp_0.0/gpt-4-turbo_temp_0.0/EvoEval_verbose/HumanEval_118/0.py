
def get_closest_vowel(word):
    """
    This function is designed to process a given word and return the nearest vowel that 
    is found in between two consonant letters, reading from the right side of the word string. 
    The case of the letters is treated as being significant, meaning 'a' and 'A' are considered 
    as two different letters.

    The word is analyzed as follows: if the word begins or ends with a vowel, these vowels are 
    not considered in the search. The function will only consider vowels that are sandwiched 
    between two consonant characters. 

    If no vowels are found that meet the conditions laid out above, the function will return 
    an empty string. 

    The function assumes that the input string consists only of English alphabetical characters. 
    Any other characters in the string will likely lead to unexpected results.

    Examples:
    Given the input "yogurt", the function will return "u", since 'u' is the nearest vowel 
    from the right side that is sandwiched between two consonants, in this case 'g' and 'r'.

    Given the input "FULL", the function will return "U", since 'U' is the single vowel that 
    is found between two consonants, in this case 'F' and 'L'.

    Given the input "quick", the function will return "", because although 'u' and 'i' are both 
    vowels, they are not sandwiched between two consonants, thus failing to meet the conditions.

    Given the input "ab", the function will return "", because the single vowel in the string, 
    'a', is at the start of the string, and is thus not sandwiched between two consonants. 

    """
    vowels = 'aeiouAEIOU'
    reversed_word = word[::-1]
    for i in range(1, len(reversed_word) - 1):
        if reversed_word[i] in vowels and (not reversed_word[i - 1] in vowels) and (not reversed_word[i + 1] in vowels):
            return reversed_word[i]
    return ''