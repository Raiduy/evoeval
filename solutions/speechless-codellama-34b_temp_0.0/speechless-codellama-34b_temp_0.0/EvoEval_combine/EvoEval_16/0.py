def get_music_notes(word: str, music_string: str):
    vowels = 'AEIOUaeiou'
    beats = {'o': 4, 'o|': 2, '.|': 1}
    notes = []
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            for j in range(len(music_string)):
                if music_string[j] == word[i]:
                    for k in range(j, len(music_string)):
                        if music_string[k] in beats:
                            notes.append(beats[music_string[k]])
                        elif music_string[k] == ' ':
                            break
                        else:
                            continue
                    break
            break
    return notes