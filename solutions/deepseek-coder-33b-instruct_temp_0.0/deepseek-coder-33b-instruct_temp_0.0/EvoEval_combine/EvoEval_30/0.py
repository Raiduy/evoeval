
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    (numerator, denominator) = map(int, x.split('/'))
    x_value = numerator / denominator
    note_values = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    results = []
    for note in notes:
        beat_value = note_values[note]
        if x_value * beat_value == int(x_value * beat_value):
            results.append(True)
        else:
            results.append(False)
    return results