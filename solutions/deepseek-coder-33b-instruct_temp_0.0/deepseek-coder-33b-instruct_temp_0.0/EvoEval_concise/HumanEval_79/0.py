
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format as a string enclosed by 'db'. 
    The binary number string contains only '0's and '1's.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = bin(decimal).replace('0b', '')
    return 'db' + binary + 'db'