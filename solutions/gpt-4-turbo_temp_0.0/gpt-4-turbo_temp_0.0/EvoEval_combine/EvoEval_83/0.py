
import re


def prime_underscored_length(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with a single underscore ("-").
    
    After the replacement, check if the length of the new string is a prime number. 
    Return True if it is a prime number, False otherwise. 
    """
    text = re.sub(' {2,}', '-', text)
    text = text.replace(' ', '_')
    return is_prime(len(text))