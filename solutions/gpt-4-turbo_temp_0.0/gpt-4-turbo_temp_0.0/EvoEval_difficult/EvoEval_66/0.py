def advancedDigitSum(s, t):
    sum_upper = 0
    sum_lower = 0
    for char in s:
        if char.isupper():
            sum_upper += ord(char)
    for char in t:
        if char.islower():
            sum_lower += ord(char)
    return (sum_upper, sum_lower)