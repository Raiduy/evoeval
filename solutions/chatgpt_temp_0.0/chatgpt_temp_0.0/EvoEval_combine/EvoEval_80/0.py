def cyclic_encode_delete(s: str, c: str) -> tuple:

    def encode(s):
        return ''.join((s[i:i + 3][j] for j in range(3) for i in range(0, len(s), 3) if i + j < len(s)))

    def decode(s):
        return ''.join((s[i // 3 + i % 3] for i in range(len(s))))
    encoded_s = encode(s)
    filtered_s = ''.join((char for char in encoded_s if char not in c))
    if filtered_s == filtered_s[::-1]:
        return (filtered_s, True)
    else:
        decoded_s = decode(filtered_s)
        return (decoded_s, False)