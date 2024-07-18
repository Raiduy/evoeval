from typing import List


def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    for note in music_string.split():
        beats.append(beat_mapping[note])
    return beats