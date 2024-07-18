from typing import List

def sort_happy_numbers(numbers: str) -> str:
    numbers_list = numbers.split()
    num_str = ''.join(numbers_list)
    for i in range(len(num_str) - 2):
        if num_str[i] == num_str[i + 1] or num_str[i] == num_str[i + 2] or num_str[i + 1] == num_str[i + 2]:
            return 'Not a happy string'
    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sorted_numbers = sorted(numbers_list, key=lambda x: numbers_dict[x])
    return ' '.join(sorted_numbers)