

def how_many_times(string: str, substring: str) -> int:
    """
    This function is designed to compute the frequency of a specific substring within a given string. The function counts all instances of the substring, including those that overlap. The function takes two inputs - the original string and the substring - both of which are of type str. The function returns an integer value which represents the count of how many times the specified substring occurs in the original string.

    The function follows these rules: 
    - If the original string is empty, it returns 0 irrespective of the substring value.
    - If the substring is found within the original string, it increments the count.
    - The function also includes overlapping instances of the substring in the count.

    Here are some examples that illustrate how this function works:
    - If you pass an empty string and 'a' as the substring, the function returns 0 since there are no characters in the original string. 
    Example: how_many_times('', 'a') returns 0

    - If you pass 'aaa' as the original string and 'a' as the substring, the function returns 3 since the substring 'a' is found three times in the original string.
    Example: how_many_times('aaa', 'a') returns 3

    - If you pass 'aaaa' as the original string and 'aa' as the substring, the function returns 3 since the substring 'aa' is found three times in the original string, counting overlapping occurrences.
    Example: how_many_times('aaaa', 'aa') returns 3
    """
    if not string:
        return 0
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count