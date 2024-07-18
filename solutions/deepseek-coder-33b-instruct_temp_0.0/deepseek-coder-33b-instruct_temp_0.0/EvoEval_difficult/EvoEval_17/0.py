from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    beat_map = {'o': 4, 'o|': 2, '.|': 1, 'r': 4, 'r|': 2, 'r.': 1}
    beats = []
    types = []
    last_beat = 0
    for item in music_string.split():
        if item in beat_map:
            beats.append(beat_map[item])
            types.append('note' if item[0] == 'o' else 'rest')
            last_beat = beat_map[item]
        else:
            beats.append(last_beat)
            types.append('note' if types[-1] == 'rest' else 'rest')
    return (beats, types)