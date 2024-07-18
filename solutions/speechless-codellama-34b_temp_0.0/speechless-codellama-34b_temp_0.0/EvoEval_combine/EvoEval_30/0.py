
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    (numerator, denominator) = map(int, x.split('/'))
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    results = []
    notes = music_string.split()
    for note in notes:
        beats = note_beats[note]
        if numerator * beats % denominator == 0:
            results.append(True)
        else:
            results.append(False)
    return results