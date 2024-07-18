def get_music_notes(word: str, music_string: str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    music_notes = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    reversed_word = word[::-1]
    reversed_music = music_string[::-1]
    for i in range(1, len(reversed_word) - 1):
        if reversed_word[i] in vowels and reversed_word[i - 1] not in vowels and (reversed_word[i + 1] not in vowels):
            note = reversed_music[i]
            beats = music_notes.get(note, 0)
            result.append(beats)
    return result