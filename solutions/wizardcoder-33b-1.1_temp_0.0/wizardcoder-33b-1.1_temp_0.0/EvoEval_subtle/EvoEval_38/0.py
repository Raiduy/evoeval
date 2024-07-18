
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of four characters.
    """
    n = 4
    # split string to groups. Each of length 4.
    groups = [s[(n * i):min((n * i + n), len(s))] for i in range((len(s) + n - 1) // n)]
    # cycle elements in each group. Unless group has fewer elements than 4.
    groups = [(group[1:] + group[0]) if len(group) == n else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    n = 4
    groups = [s[n * i:min(n * i + n, len(s))] for i in range((len(s) + n - 1) // n)]
    groups = [group[-1] + group[:-1] if len(group) == n else group for group in groups]
    return ''.join(groups)