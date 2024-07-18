
def roman_happiness(s):
    roman_dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    if len(s) < 3 or len(set(s)) != len(s):
        return False
    num = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
            num += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
        else:
            num += roman_dict[s[i]]
    if num > 1000:
        return False
    return num