from typing import List


def parse_music(music_string: str) -> List[int]:
    music_list = music_string.split()
    duration_list = []
    for note in music_list:
        if note == 'o':
            duration_list.append(4)
        elif note == 'o|':
            duration_list.append(2)
        elif note == '.|':
            duration_list.append(1)
    return duration_list