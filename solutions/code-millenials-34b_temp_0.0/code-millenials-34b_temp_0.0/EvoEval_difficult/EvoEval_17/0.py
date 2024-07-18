from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    beats = []
    types = []
    prev_beat = 4
    for item in music_string.split():
        if item == 'o':
            beats.append(4)
            types.append('note')
            prev_beat = 4
        elif item == 'o|':
            beats.append(2)
            types.append('note')
            prev_beat = 2
        elif item == '.|':
            beats.append(1)
            types.append('note')
            prev_beat = 1
        elif item == 'r':
            beats.append(4)
            types.append('rest')
            prev_beat = 4
        elif item == 'r|':
            beats.append(2)
            types.append('rest')
            prev_beat = 2
        elif item == 'r.':
            beats.append(1)
            types.append('rest')
            prev_beat = 1
        else:
            beats.append(prev_beat)
            types.append('rest')
    return (beats, types)