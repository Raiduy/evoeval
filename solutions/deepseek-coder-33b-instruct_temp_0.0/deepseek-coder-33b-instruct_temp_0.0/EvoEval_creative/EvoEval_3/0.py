from typing import List

def magical_alphabet(input_string: str) -> List[str]:

    def decode(s: str) -> str:
        return chr(int(s) + 96)

    def helper(s: str) -> List[str]:
        if not s:
            return []
        elif len(s) == 1:
            return [decode(s)]
        else:
            result = []
            if s[0] != '0':
                result += [decode(s[0]) + x for x in helper(s[1:])]
            if len(s) > 1 and '0' < s[:2] <= '26':
                result += [decode(s[:2]) + x for x in helper(s[2:])]
            return result
    return helper(input_string)