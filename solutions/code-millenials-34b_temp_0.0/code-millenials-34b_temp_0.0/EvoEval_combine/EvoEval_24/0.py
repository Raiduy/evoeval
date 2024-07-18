from typing import List

def sort_happy_numbers(numbers: str) -> str:
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers = numbers.replace(' ', '').split()
    if not all((numbers[i] != numbers[i + 1] != numbers[i + 2] for i in range(len(numbers) - 2))):
        return 'Not a happy string'
    numbers.sort(key=lambda x: number_map[x])
    return ' '.join(numbers)