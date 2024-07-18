def alien_language(word_list, alien_dictionary):
    if not word_list:
        return 'CORRECT'
    alien_dict = {char: i for (i, char) in enumerate(alien_dictionary)}
    for i in range(len(word_list) - 1):
        if sum((alien_dict[c1] > alien_dict[c2] for (c1, c2) in zip(word_list[i], word_list[i + 1]))) > 0:
            return 'INCORRECT'
    return 'CORRECT'