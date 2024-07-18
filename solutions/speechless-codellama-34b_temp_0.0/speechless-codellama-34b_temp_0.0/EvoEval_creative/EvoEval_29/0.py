def find_palindrome_substrings(s: str):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                substrings.add(substring)
    return sorted(list(substrings))