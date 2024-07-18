def circular_shift(x, shift, direction):
    if not isinstance(shift, int) or shift < 1:
        return 'Invalid Input'
    if direction not in ['R', 'L']:
        return 'Invalid Input'
    digits = str(x)
    if shift > len(digits):
        return digits[::-1]
    if direction == 'R':
        return digits[-shift:] + digits[:-shift]
    else:
        return digits[shift:] + digits[:shift]