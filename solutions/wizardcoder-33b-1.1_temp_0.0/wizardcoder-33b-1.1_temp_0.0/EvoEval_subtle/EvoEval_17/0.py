
from typing import List


def parse_music(music_string: str) -> List[int]:
    note_lengths = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    note_lengths_set = set(map(note_lengths.get, notes))
    note_lengths_list = sorted(list(note_lengths_set), reverse=True)
    return note_lengths_list