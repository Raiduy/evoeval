def sorted_happy_strings(lst):

    def is_happy(s):
        return len(s) >= 3 and all((len(set(s[i:i + 3])) == 3 for i in range(len(s) - 2)))
    happy_strings = [s for s in lst if is_happy(s)]
    happy_strings.sort(key=lambda s: (len(s), s))
    return happy_strings