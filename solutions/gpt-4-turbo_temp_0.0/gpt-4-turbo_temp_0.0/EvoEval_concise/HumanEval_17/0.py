from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Transforms a string of musical notes (represented in a special ASCII format) into a list of integers. Each integer represents the duration of a note.

    Legend:
    'o' - whole note (4 beats)
    'o|' - half note (2 beats)
    '.|' - quarter note (1 beat)

    Example: 
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    symbols = []
    i = 0
    while i < len(music_string):
        if i + 1 < len(music_string) and music_string[i + 1] == '|':
            symbols.append(music_string[i:i + 2])
            i += 2
        else:
            symbols.append(music_string[i])
            i += 1
    durations = []
    for symbol in symbols:
        if symbol == 'o':
            durations.append(4)
        elif symbol == 'o|':
            durations.append(2)
        elif symbol == '.|':
            durations.append(1)
        elif symbol == ' ':
            continue
        else:
            raise ValueError(f'Unknown symbol: {symbol}')
    return durations