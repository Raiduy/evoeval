
def split_words(txt):
    # First, try to split by whitespace
    if ' ' in txt:
        return txt.split()
    # If no whitespace, try to split by comma
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count lowercase letters with odd order in the alphabet
        odd_order_count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 0)
        return odd_order_count
