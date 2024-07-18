from typing import List

def sort_happy_numbers(numbers: str) -> str:
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_to_word = {v: k for (k, v) in word_to_num.items()}
    words = numbers.split()
    for i in range(len(words) - 2):
        if words[i] == words[i + 1] or words[i] == words[i + 2] or words[i + 1] == words[i + 2]:
            return 'Not a happy string'
    numbers = sorted([word_to_num[word] for word in words])
    sorted_words = ' '.join([num_to_word[num] for num in numbers])
    return sorted_words