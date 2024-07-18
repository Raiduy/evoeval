
def hex_key(num):
    prime_hexes = set('2357BD')
    count = 0
    for char in num:
        if char in prime_hexes:
            count += 1
    return count