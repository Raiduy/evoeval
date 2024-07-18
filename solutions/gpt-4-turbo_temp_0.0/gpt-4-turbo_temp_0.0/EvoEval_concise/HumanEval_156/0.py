
def int_to_mini_roman(number):
    """
    Converts a positive integer (1 <= num <= 1000) into its lowercase roman numeral string equivalent.

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_numerals = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    roman_string = ''
    for (value, symbol) in roman_numerals:
        while number >= value:
            roman_string += symbol
            number -= value
    return roman_string