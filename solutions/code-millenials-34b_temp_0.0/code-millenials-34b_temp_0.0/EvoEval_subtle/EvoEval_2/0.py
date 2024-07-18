
def truncate_number(number: float) -> float:
    integer_part = int(number)
    decimal_part = number - integer_part
    return (integer_part, decimal_part)