from typing import List

def count_animals(animal_string: str) -> List[int]:
    animal_counts = {'C': 0, 'D': 0, 'B': 0}
    animal_sounds = {'C': 'meow', 'D': 'woof', 'B': 'chirp'}
    animal_order = []
    animal_sounds_count = []
    animal_string_list = animal_string.split()
    for animal_sound in animal_string_list:
        animal = animal_sound[0]
        sound = animal_sound[1:]
        if animal in animal_counts and animal_counts[animal] < 2 and (sound == animal_sounds[animal]):
            animal_counts[animal] += 1
            if animal not in animal_order:
                animal_order.append(animal)
            animal_sounds_count.append(len(sound))
        if len(animal_order) == 5:
            break
    return animal_sounds_count