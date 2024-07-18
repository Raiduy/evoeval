def odd_count_base_change(lst, base):

    def digit_to_base(digit, base):
        """Convert a single digit to the given base and return it as a string."""
        if digit < base:
            return str(digit)
        else:
            return digit_to_base(digit // base, base) + str(digit % base)

    def count_odd_digits_in_base(s, base):
        """Convert each digit in the string to the given base and count the odd digits."""
        count = 0
        for char in s:
            converted = digit_to_base(int(char), base)
            count += sum((1 for c in converted if c in '13579'))
        return count
    result = []
    for s in lst:
        odd_count = count_odd_digits_in_base(s, base)
        output_str = f'the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.'
        result.append(output_str)
    return result