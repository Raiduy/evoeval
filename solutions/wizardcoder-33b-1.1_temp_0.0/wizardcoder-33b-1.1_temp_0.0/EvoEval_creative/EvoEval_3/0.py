from typing import List

def magical_alphabet(input_string: str) -> List[str]:

    def decode(s):
        if not s:
            return ['']
        elif len(s) == 1:
            return [chr(int(s) + 96)]
        else:
            result = []
            if s[0] != '0':
                for c in decode(s[1:]):
                    result.append(chr(int(s[:1]) + 96) + c)
            if 10 <= int(s[:2]) <= 26:
                for c in decode(s[2:]):
                    result.append(chr(int(s[:2]) + 96) + c)
            return result
    return decode(input_string)