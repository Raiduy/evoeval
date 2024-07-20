from typing import List

def count_animals(animal_string: str) -> List[int]:
    """ 
    Input to this function is a string representing animals and their sounds in a special ASCII format. 
    Your task is to parse this string and return a list of integers corresponding to how many times each 
    animal made a sound.

    Here is a legend:
    'C' - Cat, makes sound 'meow'
    'D' - Dog, makes sound 'woof'
    'B' - Bird, makes sound 'chirp'

    Each sound is represented by a '|', and each animal-sound pair is separated by a space.

    For example, a 'Cat' making sound 3 times will be represented as 'C|||'.

    The function should return a list of integers representing how many sounds each animal made, in the order 
    they appear in the string. Skip invalid animals and also skip animals that has already appeared twice before. Furthermore, skip any animals after total animals (invalid and valid) has reached 5

    >>> count_animals('C||| D|| B| C| B||| D|||')
    [3, 2, 1, 1, 3]
    """
    animal_counts = {'C': 0, 'D': 0, 'B': 0}
    total_animals = 0
    result = []
    for animal_sound in animal_string.split():
        if total_animals >= 5:
            break
        animal = animal_sound[0]
        sound = animal_sound[1:]
        if animal in animal_counts and animal_counts[animal] < 2:
            animal_counts[animal] += 1
            total_animals += 1
            result.append(sound.count('|'))
    return result