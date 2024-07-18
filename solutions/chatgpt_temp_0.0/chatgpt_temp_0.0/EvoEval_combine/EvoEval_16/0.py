def get_music_notes(word: str, music_string: str):
    vowels = 'aeiouAEIOU'
    vowels_indices = [i for (i, char) in enumerate(word) if char in vowels]
    if len(vowels_indices) < 2:
        return []
    closest_vowel_index = vowels_indices[-2]
    beats = []
    for i in range(closest_vowel_index, len(word)):
        if word[i] in vowels:
            break
        if word[i] != ' ':
            if music_string[i] == 'o':
                beats.append(4)
            elif music_string[i] == '|':
                beats.append(2)
            elif music_string[i] == '.':
                beats.append(1)
    return beats