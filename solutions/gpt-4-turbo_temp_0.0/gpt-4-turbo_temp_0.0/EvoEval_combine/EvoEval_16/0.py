def get_music_notes(word: str, music_string: str):
    vowels = 'aeiouAEIOU'
    notes = music_string.split()
    note_values = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    vowel_pos = -1
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            vowel_pos = i
            break
    if vowel_pos == -1:
        return result
    for note in notes[:vowel_pos + 1]:
        if note in note_values:
            result.append(note_values[note])
        else:
            pass
    return result