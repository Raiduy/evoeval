from typing import List

def count_animals(animal_string: str) -> List[int]:
    animal_counts = {'C': 0, 'D': 0, 'B': 0}
    result = []
    animal_list = animal_string.split()
    for animal in animal_list:
        if animal[0] in animal_counts and animal_counts[animal[0]] < 2 and (len(result) < 5):
            result.append(animal.count('|'))
            animal_counts[animal[0]] += 1
    return result