from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    legend = {'o': (4, 'note'), 'o|': (2, 'note'), '.|': (1, 'note'), 'r': (4, 'rest'), 'r|': (2, 'rest'), 'r.': (1, 'rest')}
    beats = []
    types = []
    items = music_string.split()
    last_valid_beat = 1
    for item in items:
        if item in legend:
            (beat, type_) = legend[item]
            last_valid_beat = beat
        else:
            (beat, type_) = (last_valid_beat, 'rest')
        beats.append(beat)
        types.append(type_)
    return (beats, types)