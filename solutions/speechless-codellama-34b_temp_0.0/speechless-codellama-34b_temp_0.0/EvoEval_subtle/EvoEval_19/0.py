
from typing import List


def sort_numbers(numbers: str) -> str:
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    words = numbers.split()
    nums = [word_to_num[word] for word in words]
    nums.sort(reverse=True)
    sorted_words = [str(num) for num in nums]
    sorted_numbers = ' '.join(sorted_words)
    return sorted_numbers