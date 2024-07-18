def sorted_happy_strings(lst):
    happy_strings = []
    for string in lst:
        if len(string) >= 3:
            is_happy = True
            for i in range(len(string) - 2):
                if string[i] == string[i + 1] or string[i] == string[i + 2] or string[i + 1] == string[i + 2]:
                    is_happy = False
                    break
            if is_happy:
                happy_strings.append(string)
    happy_strings.sort(key=lambda x: (len(x), x))
    return happy_strings