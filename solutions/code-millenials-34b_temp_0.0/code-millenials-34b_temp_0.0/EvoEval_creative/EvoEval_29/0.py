def find_palindrome_substrings(s: str):

    def is_palindrome(s: str):
        return s == s[::-1]
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return sorted(list(palindromes))