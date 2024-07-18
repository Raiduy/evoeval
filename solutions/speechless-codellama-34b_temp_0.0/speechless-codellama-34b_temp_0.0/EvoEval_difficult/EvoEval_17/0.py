from typing import List, Tuple


def parse_music_advanced(music_string: str) -> Tuple[List[int], List[str]]:
    notes = []
    rests = []
    beats = []
    types = []
    for item in music_string.split():
        if item == 'o':
            notes.append(4)
            types.append('note')
        elif item == 'o|':
            notes.append(2)
            types.append('note')
        elif item == '.|':
            notes.append(1)
            types.append('note')
        elif item == 'r':
            rests.append(4)
            types.append('rest')
        elif item == 'r|':
            rests.append(2)
            types.append('rest')
        elif item == 'r.':
            rests.append(1)
            types.append('rest')
        elif notes:
            beats.append(notes[-1])
            types.append('rest')
        elif rests:
            beats.append(rests[-1])
            types.append('rest')
        else:
            beats.append(1)
            types.append('rest')
    return (beats, types)