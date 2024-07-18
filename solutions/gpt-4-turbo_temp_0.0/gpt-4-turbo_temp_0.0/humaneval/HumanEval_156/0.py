
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Define a list of Roman numeral symbols and their corresponding values
    roman_numerals = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    
    # Initialize an empty string to store the result
    roman_string = ''
    
    # Loop through each symbol and value in the list
    for value, symbol in roman_numerals:
        # While the number is greater than or equal to the value
        while number >= value:
            # Append the symbol to the result string
            roman_string += symbol
            # Subtract the value from the number
            number -= value
            
    return roman_string
