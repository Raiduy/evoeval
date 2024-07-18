
import re


def prime_underscored_length(text):
    text = re.sub('\\s', '_', text)
    text = re.sub('\\s+', '-', text)
    length = len(text)
    if length < 2:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True