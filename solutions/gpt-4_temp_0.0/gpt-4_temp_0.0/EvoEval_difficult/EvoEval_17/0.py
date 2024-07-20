from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    legend = {'o': 4, 'o|': 2, '.|': 1, 'r': 4, 'r|': 2, 'r.': 1}
    music_list = music_string.split()
    beats = []
    types = []
    prev_beat = 0
    for item in music_list:
        if item in legend:
            beats.append(legend[item])
            prev_beat = legend[item]
            if 'r' in item:
                types.append('rest')
            else:
                types.append('note')
        else:
            beats.append(prev_beat)
            types.append('rest')
    return (beats, types)