
from typing import List


def parse_music(music_string: str) -> List[int]:
    beat_values = []
    for note in music_string.split():
        if note == 'o':
            beat_values.append(4)
        elif note == 'o|':
            beat_values.append(2)
        elif note == '.|':
            beat_values.append(1)
    unique_beats = list(set(beat_values))
    unique_beats.sort(reverse=True)
    return unique_beats