def alien_language(word_list, alien_dictionary):
    if not word_list:
        return 'CORRECT'
    alien_order = {char: i for (i, char) in enumerate(alien_dictionary)}
    for i in range(len(word_list) - 1):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if alien_order[word1[j]] > alien_order[word2[j]]:
                    return 'INCORRECT'
                break
        else:
            if len(word1) > len(word2):
                return 'INCORRECT'
    return 'CORRECT'