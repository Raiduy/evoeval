
def encode(message):
    vowels = 'aeiouAEIOU'
    trans = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZ123', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = message.translate(trans)
    for v in vowels:
        message = message.replace(v, chr(ord(v) + 2))
    return message.swapcase()