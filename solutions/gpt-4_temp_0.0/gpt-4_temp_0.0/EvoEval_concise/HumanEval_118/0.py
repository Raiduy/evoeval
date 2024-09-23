
def get_closest_vowel(word):
    """Find the rightmost vowel that is surrounded by consonants in a given word. 

    Only consider vowels that are not at the start or end of the word. If no such vowel exists, 
    return an empty string. The function is case sensitive.

    The input word only contains English letters.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = 'aeiouAEIOU'
    closest_vowel = ''
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            closest_vowel = word[i]
    return closest_vowel