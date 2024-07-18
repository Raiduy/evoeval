def prime_cipher(s: str):
    result = ''
    for char in s:
        if char.islower():
            prime_num = get_prime_number(ord(char) - ord('a') + 1)
            result += str(prime_num)
        else:
            result += char
    return result