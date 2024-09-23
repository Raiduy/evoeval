def get_music_notes(word: str, music_string: str):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    music_notes = music_string.split()
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] in consonants and (word[i + 1] in consonants):
            for j in range(i + 1):
                beats.append(music_dict[music_notes[j]])
            return beats
    return []