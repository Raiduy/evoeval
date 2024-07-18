def alien_language(word_list, alien_dictionary):
    alien_dict_map = {letter: index for (index, letter) in enumerate(alien_dictionary)}
    for i in range(len(word_list) - 1):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        for j in range(min(len(word1), len(word2))):
            letter1 = word1[j]
            letter2 = word2[j]
            if alien_dict_map[letter1] > alien_dict_map[letter2]:
                return 'INCORRECT'
            elif alien_dict_map[letter1] < alien_dict_map[letter2]:
                break
        else:
            if len(word1) > len(word2):
                return 'INCORRECT'
    return 'CORRECT'