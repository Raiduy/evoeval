from typing import List


def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    notes = music_string.split()
    for note in notes:
        beats.append(beat_mapping[note])
    return beats