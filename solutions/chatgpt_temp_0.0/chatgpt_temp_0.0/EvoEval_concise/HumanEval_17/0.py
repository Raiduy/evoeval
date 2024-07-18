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
    durations = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    return [durations[note] for note in notes]