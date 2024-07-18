from typing import List

def sort_happy_numbers(numbers: str) -> str:
    num_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    for i in range(len(num_list) - 2):
        if num_list[i] == num_list[i + 1] or num_list[i] == num_list[i + 2] or num_list[i + 1] == num_list[i + 2]:
            return 'Not a happy string'
    num_list.sort(key=lambda x: num_map[x])
    sorted_numbers = ' '.join(num_list)
    return sorted_numbers