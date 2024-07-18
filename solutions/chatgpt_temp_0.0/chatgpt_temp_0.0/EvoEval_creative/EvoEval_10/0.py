from typing import List

def count_animals(animal_string: str) -> List[int]:
    animals = {'C': 'meow', 'D': 'woof', 'B': 'chirp'}
    animal_counts = {}
    result = []
    total_animals = 0
    for animal_sound_pair in animal_string.split():
        if total_animals >= 5:
            break
        (animal, sound) = animal_sound_pair.split('|')
        if animal in animals and animals[animal] == sound and (animal not in animal_counts):
            animal_counts[animal] = animal_counts.get(animal, 0) + 1
            result.append(animal_counts[animal])
            total_animals += 1
    return result