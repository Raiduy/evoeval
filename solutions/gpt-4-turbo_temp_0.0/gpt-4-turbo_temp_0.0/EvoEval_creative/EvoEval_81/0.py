def alien_language(word_list, alien_dictionary):
    alien_dict_index = {char: index for (index, char) in enumerate(alien_dictionary)}

    def alien_value(word):
        return [alien_dict_index[char] for char in word]
    for i in range(len(word_list) - 1):
        current_word_value = alien_value(word_list[i])
        next_word_value = alien_value(word_list[i + 1])
        if next_word_value < current_word_value:
            return 'INCORRECT'
    return 'CORRECT'