from typing import List

def magical_alphabet(input_string: str) -> List[str]:

    def helper(index, current):
        if index == len(input_string):
            result.append(current)
            return
        for i in range(1, 4):
            if index + i <= len(input_string):
                num = int(input_string[index:index + i])
                if 1 <= num <= 26:
                    helper(index + i, current + chr(ord('a') + num - 1))
    result = []
    helper(0, '')
    return result