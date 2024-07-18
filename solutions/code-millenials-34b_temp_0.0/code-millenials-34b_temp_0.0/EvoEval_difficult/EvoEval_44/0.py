def change_base(x: str, base: int, new_base: int):
    for digit in x:
        if not digit.isdigit():
            if ord('A') <= ord(digit) <= ord('Z') and ord(digit) - ord('A') >= base - 10:
                return 'invalid base'
            if ord('a') <= ord(digit) <= ord('z') and ord(digit) - ord('a') >= base - 10:
                return 'invalid base'
    decimal = 0
    for i in range(len(x)):
        digit = x[len(x) - 1 - i]
        if digit.isdigit():
            decimal += int(digit) * base ** i
        else:
            decimal += (ord(digit.upper()) - ord('A')) * base ** i
    result = ''
    while decimal > 0:
        remainder = decimal % new_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder + ord('A')) + result
        decimal //= new_base
    return result