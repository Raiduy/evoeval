
from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of unique integers corresponding to how many beats does each
    note last. Return the list in descending order.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1]
    """
    beat_values = set()
    notes = music_string.split()
    for note in notes:
        if note == 'o':
            beat_values.add(4)
        elif note == 'o|':
            beat_values.add(2)
        elif note == '.|':
            beat_values.add(1)
    beat_values = list(beat_values)
    beat_values.sort(reverse=True)
    return beat_values