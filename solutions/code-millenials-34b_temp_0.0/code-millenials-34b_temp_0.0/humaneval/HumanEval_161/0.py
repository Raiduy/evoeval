
def solve(s):
    new_s = ""
    for i in s:
        if i.isalpha():
            new_s += i.swapcase()
        else:
            new_s += i
    if not any(char.isalpha() for char in s):
        new_s = new_s[::-1]
    return new_s
