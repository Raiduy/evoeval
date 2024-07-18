def advancedDigitSum(s, t):
    sum_s = 0
    sum_t = 0
    for char in s:
        if char.isupper():
            sum_s += ord(char)
    for char in t:
        if char.islower():
            sum_t += ord(char)
    return (sum_s, sum_t)