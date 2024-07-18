def alien_language(word_list, alien_dictionary):
    if not word_list:
        return 'CORRECT'
    alien_dict = {char: i for (i, char) in enumerate(alien_dictionary)}
    for i in range(len(word_list) - 1):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        for j in range(min(len(word1), len(word2))):
            if alien_dict[word1[j]] < alien_dict[word2[j]]:
                break
            elif alien_dict[word1[j]] > alien_dict[word2[j]]:
                return 'INCORRECT'
        if len(word1) > len(word2):
            return 'INCORRECT'
    return 'CORRECT'