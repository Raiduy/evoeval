from typing import List


def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    i = 0
    while i < len(music_string):
        if music_string[i:i + 2] in beat_mapping:
            beats.append(beat_mapping[music_string[i:i + 2]])
            i += 2
        elif music_string[i] in beat_mapping:
            beats.append(beat_mapping[music_string[i]])
            i += 1
        else:
            i += 1
    return beats