def advancedDigitSum(s, t):
    sum_s = sum((ord(c) for c in s if c.isupper()))
    sum_t = sum((ord(c) for c in t if c.islower()))
    return (sum_s, sum_t)