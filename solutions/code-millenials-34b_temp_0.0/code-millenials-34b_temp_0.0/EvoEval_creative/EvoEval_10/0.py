from typing import List

def count_animals(animal_string: str) -> List[int]:
    sound_dict = {'C': 'meow', 'D': 'woof', 'B': 'chirp'}
    animal_dict = {'C': 0, 'D': 0, 'B': 0}
    sound_list = animal_string.split()
    count_list = []
    count = 0
    for sound in sound_list:
        animal = sound[0]
        if animal in sound_dict and animal_dict[animal] < 2 and (count < 5):
            sound_count = sound.count('|')
            count_list.append(sound_count)
            animal_dict[animal] += 1
            count += 1
    return count_list