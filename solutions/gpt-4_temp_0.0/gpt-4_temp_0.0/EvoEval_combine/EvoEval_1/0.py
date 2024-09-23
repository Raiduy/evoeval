def round_and_flip(value: str) -> str:
    (number, text) = (''.join(filter(lambda i: i.isdigit() or i == '.' or i == '-', value)), ''.join(filter(lambda i: i.isalpha(), value)))
    number = round(float(number))
    text = text.swapcase()
    return f'{number} {text}'