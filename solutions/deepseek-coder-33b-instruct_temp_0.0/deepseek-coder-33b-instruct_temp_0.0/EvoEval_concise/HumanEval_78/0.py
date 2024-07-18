
def hex_key(num):
    """This function receives a hexadecimal number as a string and 
    counts the number of hexadecimal digits that are prime numbers.
    The prime numbers in hexadecimal digits are 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    It's assumed the input is always correct or an empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count