from typing import List

def magical_alphabet(input_string: str) -> List[int]:

    def dfs(s: str, path: str, res: List[str]):
        if not s:
            res.append(path)
            return
        if 0 < int(s[:1]) <= 9:
            dfs(s[1:], path + chr(int(s[:1]) + 96), res)
        if 10 <= int(s[:2]) <= 26:
            dfs(s[2:], path + chr(int(s[:2]) + 96), res)
    result = []
    dfs(input_string, '', result)
    return result