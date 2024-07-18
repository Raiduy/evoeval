from typing import List

def sort_happy_numbers(numbers: str) -> str:
    numeral_to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers = numbers.replace(' ', '')
    for i in range(len(numbers) - 2):
        if numbers[i] == numbers[i + 1] or numbers[i] == numbers[i + 2] or numbers[i + 1] == numbers[i + 2]:
            return 'Not a happy string'
    numbers_list = [numeral_to_int[num] for num in numbers]
    numbers_list.sort()
    sorted_numbers = ' '.join([str(num) for num in numbers_list])
    return sorted_numbers