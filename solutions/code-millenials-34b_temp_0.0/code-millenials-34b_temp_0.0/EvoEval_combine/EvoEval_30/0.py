
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    (numerator, denominator) = map(int, x.split('/'))
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music_notes = music_string.split()
    result = []
    for note in music_notes:
        beats = notes.get(note, 0)
        if numerator * beats % denominator == 0:
            result.append(True)
        else:
            result.append(False)
    return result