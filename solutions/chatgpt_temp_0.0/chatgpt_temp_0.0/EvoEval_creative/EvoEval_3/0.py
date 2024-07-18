from typing import List

def magical_alphabet(input_string: str) -> List[int]:

    def backtrack(index: int, path: str) -> None:
        if index == len(input_string):
            combinations.append(path)
            return
        if input_string[index] != '0':
            char = chr(ord('a') + int(input_string[index]) - 1)
            backtrack(index + 1, path + char)
        if index + 1 < len(input_string) and input_string[index] != '0' and (int(input_string[index:index + 2]) <= 26):
            char = chr(ord('a') + int(input_string[index:index + 2]) - 1)
            backtrack(index + 2, path + char)
    combinations = []
    backtrack(0, '')
    return combinations