
import re


def prime_underscored_length(text):
    new_text = re.sub(' +', '_', text)
    return is_prime(len(new_text))