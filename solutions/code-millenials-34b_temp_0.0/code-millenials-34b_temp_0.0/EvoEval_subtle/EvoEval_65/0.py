
def circular_shift(x, shift):
    digits = [int(d) for d in str(x)]
    if shift >= len(digits):
        return str(x)[::-1]
    else:
        return str(digits[shift:] + digits[:shift])