def reverse_vowels(s):
    """Given a string s, return a new string with the vowels in reverse order, while keeping the position of other characters unchanged.
    The string can contain uppercase and lowercase letters.
    For example:
    reverse_vowels('Hello') == 'Holle'
    reverse_vowels('Python') == 'Python'
    reverse_vowels('algorithm') == 'ilgorathm'
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_list = list(s)
    (i, j) = (0, len(s_list) - 1)
    while i < j:
        if s_list[i] in vowels and s_list[j] in vowels:
            (s_list[i], s_list[j]) = (s_list[j], s_list[i])
            i += 1
            j -= 1
        elif s_list[i] in vowels:
            j -= 1
        elif s_list[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(s_list)