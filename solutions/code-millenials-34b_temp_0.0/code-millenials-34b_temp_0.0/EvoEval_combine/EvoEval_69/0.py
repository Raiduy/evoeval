def sorted_happy_strings(lst):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) != 3:
                return False
        return True
    lst = [s for s in lst if is_happy(s) and len(s) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst