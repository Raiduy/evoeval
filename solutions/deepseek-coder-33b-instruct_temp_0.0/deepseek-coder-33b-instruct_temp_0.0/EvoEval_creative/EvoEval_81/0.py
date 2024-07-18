def alien_language(word_list, alien_dictionary):
    """
    An alien civilization has its own dictionary to define the order of their alphabet letters.
    This dictionary is a string of all lowercase letters from 'a' to 'z' but not 
    necessarily in the English alphabetic order. For example, the alien dictionary may be 'hijklmnopqrstuvwxyzabcdefg'.
    A word in this alien language is a sequence of characters. 
    You are given a sorted list of words (sorted according to the alien dictionary's order)
    and the alien dictionary itself.
    Your task is to verify if the given list of words is sorted correctly in ascending order according to the alien dictionary.
    If yes, then return "CORRECT", otherwise return "INCORRECT".
    If the word list is empty, return "CORRECT".

    [input/output] samples:
    alien_language(['cat', 'dog', 'elephant'], 'abcdefghijklmnopqrstuvwxyz') => "CORRECT"
    alien_language(['apple', 'banana', 'kiwi'], 'zyxwvutsrqponmlkjihgfedcba') => "INCORRECT"
    alien_language(['bee', 'ant', 'cat', 'dog'], 'bacdefghijklmnopqrstuvwxyz') => "CORRECT"
    alien_language([], 'bacdefghijklmnopqrstuvwxyz') => "CORRECT"
    """
    if not word_list:
        return 'CORRECT'
    alien_order = {char: index for (index, char) in enumerate(alien_dictionary)}
    for i in range(1, len(word_list)):
        word1 = word_list[i - 1]
        word2 = word_list[i]
        for j in range(min(len(word1), len(word2))):
            if alien_order[word1[j]] < alien_order[word2[j]]:
                break
            elif alien_order[word1[j]] > alien_order[word2[j]]:
                return 'INCORRECT'
            elif j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2):
                return 'INCORRECT'
    return 'CORRECT'