def parse_arguments(args: list):
    """Extracts and verifies arguments from a list of mixed data types.

    The list is expected to contain one string, one integer and one list of integers, in any order.
    The string should represent a mathematical operation (either 'sum' or 'product').

    If the arguments are not as expected, it returns the string "Invalid arguments".

    Args:
    args (list): A list containing a string, an integer and a list of integers.

    Returns:
    str: The mathematical operation.
    int: The number.
    list: The list of numbers.

    Examples:
    >>> parse_arguments(['sum', 3, [1, 2, 3, 4]])
    ('sum', 3, [1, 2, 3, 4])
    >>> parse_arguments([2, [2, 3], 'product'])
    ('product', 2, [2, 3])
    >>> parse_arguments([1, 2, 3])
    'Invalid arguments'
    """
    operation = [x for x in args if type(x) is str]
    number = [x for x in args if type(x) is int]
    numbers = [x for x in args if type(x) is list]

    if len(operation) != 1 or len(number) != 1 or len(numbers) != 1:
        return "Invalid arguments"

    return operation[0], number[0], numbers[0]
def perform_operation(args: list):
    """Parses the arguments and performs a mathematical operation on a list of numbers.

    The arguments contain one string, one integer number and one list of integers, in any order.
    The string should represent a mathematical operation and can be
    either 'sum' or 'product'. The operation is performed on each number in the list,
    and the result is increased by the specified number. The function returns the total sum
    or product. If the arguments are invalid or not correctly formatted, return 'Invalid arguments'

    Args:
    args (list): A list containing a string representing the operation, an integer to increase the result
    and a list of integers.

    Returns:
    int: The total sum or product.

    Examples:
    >>> perform_operation(['sum', 3, [1, 2, 3, 4]])
    13
    >>> perform_operation([2, [2, 3], 'product'])
    8
    """
    parsed_args = parse_arguments(args)
    if parsed_args == 'Invalid arguments':
        return 'Invalid arguments'
    (operation, number, numbers) = parsed_args
    if operation == 'sum':
        result = sum(numbers) + number
    elif operation == 'product':
        result = 1
        for num in numbers:
            result *= num
        result += number
    else:
        return 'Invalid arguments'
    return result