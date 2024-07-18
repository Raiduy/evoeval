
def roman_happiness(s):
    roman_numerals = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    values = [roman_numerals[ch] for ch in s]
    if len(values) < 3 or any((values[i] >= values[i + 1] for i in range(len(values) - 1))) or any((values[i] == values[i + 2] for i in range(len(values) - 2))):
        return False
    num = 0
    for i in range(len(values)):
        if i > 0 and values[i] > values[i - 1]:
            num += values[i] - 2 * values[i - 1]
        else:
            num += values[i]
    return num