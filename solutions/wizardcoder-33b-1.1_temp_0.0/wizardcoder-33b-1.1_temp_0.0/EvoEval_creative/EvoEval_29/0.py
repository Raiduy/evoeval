def find_palindrome_substrings(s: str):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return sorted(list(palindromes))