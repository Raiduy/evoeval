
def select_words(s, n):
    """
    This function named 'select_words' is designed to process a provided string 's' and a natural number 'n'. 
    The purpose of this function is to retrieve all words from the input string 's' that contain exactly 'n' number of consonants, 
    and return them as a list in the same order as they are encountered in the string 's'.

    A consonant can be defined as any letter in the alphabet that is not a vowel (a, e, i, o, u). The function counts 
    the number of consonants in each word and if the count equals 'n', the word is added to the output list.

    If the input string 's' is empty (i.e., it doesn't contain any characters or it only contains white spaces), 
    then the function should return an empty list.

    The function makes the assumption that the input string only contains alphabetic characters and spaces, it doesn't account 
    for any other special characters, numbers or punctuation.

    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]

    In the first example, the word "little" is the only word that contains exactly 4 consonants, hence it's the only 
    word in the output list. Similarly, in the second example, the words "Mary" and "lamb" both contain exactly 3 consonants, 
    and hence, they are the words in the output list. If no words with 'n' consonants are found, as in the third example, 
    an empty list is returned.
    """
    vowels = set('aeiou')
    words = s.split()
    result = []
    for word in words:
        consonants_count = sum((1 for c in word.lower() if c.isalpha() and c not in vowels))
        if consonants_count == n:
            result.append(word)
    return result