from typing import List

def count_animals(animal_string: str) -> List[int]:
    """ 
    Parses the input string and returns a list of integers corresponding to how many times each 
    animal made a sound.
    """
    animal_sound_pairs = animal_string.split()
    animal_counts = {'C': 0, 'D': 0, 'B': 0}
    sound_counts = []
    total_animals_processed = 0
    for pair in animal_sound_pairs:
        if total_animals_processed >= 5:
            break
        total_animals_processed += 1
        if pair[0] in animal_counts and animal_counts[pair[0]] < 2:
            num_sounds = pair.count('|')
            sound_counts.append(num_sounds)
            animal_counts[pair[0]] += 1
    return sound_counts