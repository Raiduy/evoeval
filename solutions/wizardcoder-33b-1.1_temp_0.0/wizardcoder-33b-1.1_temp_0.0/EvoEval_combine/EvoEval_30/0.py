
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    notes = music_string.split()
    (numerator, denominator) = map(int, x.split('/'))
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    return [(numerator * note_to_beats[note] / denominator).is_integer() for note in notes]