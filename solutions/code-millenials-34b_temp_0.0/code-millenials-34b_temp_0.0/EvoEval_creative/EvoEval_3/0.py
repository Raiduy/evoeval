from typing import List

def magical_alphabet(input_string: str) -> List[str]:
    alphabet = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            combinations.append(combination)
        else:
            for i in range(1, len(next_digits) + 1):
                curr_str = next_digits[:i]
                if curr_str in alphabet:
                    backtrack(combination + alphabet[curr_str], next_digits[i:])
    combinations = []
    backtrack('', input_string)
    return combinations