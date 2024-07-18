
def decimal_to_binary(decimal):
    """
    This function is designed to convert a given decimal number into its binary representation. 

    The input to the function should be a decimal number, which will be transformed into binary format. The output will be a string, where each character within the string represents a digit of the binary number. Each digit will either be '0' or '1', corresponding to the binary notation.

    To assist with formatting, the returned binary string will be enclosed within an extra couple of characters 'db' both at the start and at the end of the string. These characters are not part of the binary representation of the number and are purely for formatting purposes.

    For instance, if the input to the function is the decimal number 15, the binary representation for 15 is '1111', and the return of the function will be "db1111db". As another example, if the input is the decimal number 32, the binary representation for 32 is '100000', and the return of the function will be "db100000db".

    Parameters:
    decimal (int): This is the decimal number that will be converted into binary. 

    Returns:
    str: The return value is a string which represents the binary form of the provided decimal number, enclosed within 'db' at both ends for formatting.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = bin(decimal).replace('0b', '')
    return 'db' + binary + 'db'