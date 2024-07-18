
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    (numerator, denominator) = map(int, x.split('/'))
    result = []
    notes = music_string.split()
    note_values = {'o': 4, 'o|': 2, '.|': 1}
    for note in notes:
        if note in note_values:
            beats = note_values[note]
        else:
            beats = 0
        if numerator * beats % denominator == 0:
            result.append(True)
        else:
            result.append(False)
    return result