def get_music_notes(word: str, music_string: str):
    vowels = 'aeiouAEIOU'
    notes = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            music_notes = music_string.split()
            for j in range(i + 1):
                result.append(notes[music_notes[j]])
            break
    return result