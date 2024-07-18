from typing import List


def parse_music(music_string: str) -> List[int]:
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    i = 0
    while i < len(music_string):
        if i < len(music_string) - 1 and music_string[i:i + 2] in note_to_beats:
            beats.append(note_to_beats[music_string[i:i + 2]])
            i += 2
        elif music_string[i] in note_to_beats:
            beats.append(note_to_beats[music_string[i]])
            i += 1
        else:
            i += 1
    return beats