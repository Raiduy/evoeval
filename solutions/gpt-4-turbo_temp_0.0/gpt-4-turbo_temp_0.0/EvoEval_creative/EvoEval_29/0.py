def find_palindrome_substrings(s: str):
    """
    Given a string, find all unique substrings that are palindromes.
    
    A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
    
    Return a list of all unique palindrome substrings, sorted in ascending order.
    """

    def expand_around_center(left: int, right: int):
        """
        Expand around the center of the palindrome.
        """
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            palindrome_substrings.add(s[left:right + 1])
            left -= 1
            right += 1
    palindrome_substrings = set()
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return sorted(list(palindrome_substrings))