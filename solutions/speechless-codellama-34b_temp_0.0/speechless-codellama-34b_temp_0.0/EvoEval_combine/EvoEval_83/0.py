
import re


def prime_underscored_length(text):
    text = re.sub(' {2,}', '_', text)
    text = re.sub(' ', '_', text)
    return is_prime(len(text))