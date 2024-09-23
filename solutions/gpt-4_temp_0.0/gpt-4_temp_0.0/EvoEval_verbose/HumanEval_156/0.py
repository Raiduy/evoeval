
def int_to_mini_roman(number):
    """
    This function, int_to_mini_roman, is designed to take a single input, 'number', which is expected to be a positive integer ranging from 1 to 1000, inclusive (i.e., 1 <= number <= 1000).

    The function's purpose is to convert the given integer into its corresponding roman numeral equivalent. Roman numerals are a numeral system originating from ancient Rome, where certain letters represent different values. For example, 'I' represents 1, 'V' represents 5, 'X' represents 10, 'L' represents 50, 'C' represents 100, 'D' represents 500, and 'M' represents 1000.

    The function will then output this roman numeral equivalent as a string in lowercase letters.

    As an illustration, consider the following examples:

    Given the input integer 19, the function will output the string 'xix', which is the roman numeral equivalent of 19 in lowercase letters.
    >>> int_to_mini_roman(19) == 'xix'

    Given the input integer 152, the function will output the string 'clii', which is the roman numeral equivalent of 152 in lowercase letters.
    >>> int_to_mini_roman(152) == 'clii'

    Given the input integer 426, the function will output the string 'cdxxvi', which is the roman numeral equivalent of 426 in lowercase letters.
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num