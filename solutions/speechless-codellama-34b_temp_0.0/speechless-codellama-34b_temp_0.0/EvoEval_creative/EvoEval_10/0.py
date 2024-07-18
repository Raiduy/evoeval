from typing import List

def count_animals(animal_string: str) -> List[int]:
    animals = {'C': 0, 'D': 0, 'B': 0}
    sounds = {'C': 0, 'D': 0, 'B': 0}
    result = []
    for animal_sound in animal_string.split():
        animal = animal_sound[0]
        sound_count = len(animal_sound) - 1
        if animal in animals and animals[animal] < 2 and (sounds[animal] + sound_count <= 5):
            sounds[animal] += sound_count
            animals[animal] += 1
            result.append(sound_count)
    return result