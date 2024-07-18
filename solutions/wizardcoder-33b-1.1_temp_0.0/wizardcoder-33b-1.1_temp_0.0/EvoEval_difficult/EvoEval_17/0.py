from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    music_items = music_string.split()
    beats = []
    types = []
    last_beat = 0
    for item in music_items:
        if item == 'o':
            beats.append(4)
            types.append('note')
            last_beat = 4
        elif item == 'o|':
            beats.append(2)
            types.append('note')
            last_beat = 2
        elif item == '.|':
            beats.append(1)
            types.append('note')
            last_beat = 1
        elif item == 'r':
            beats.append(4)
            types.append('rest')
            last_beat = 4
        elif item == 'r|':
            beats.append(2)
            types.append('rest')
            last_beat = 2
        elif item == 'r.':
            beats.append(1)
            types.append('rest')
            last_beat = 1
        else:
            beats.append(last_beat)
            types.append('rest')
    return (beats, types)