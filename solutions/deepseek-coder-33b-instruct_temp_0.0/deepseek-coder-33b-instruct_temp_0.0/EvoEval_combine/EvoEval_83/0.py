
import re


def prime_underscored_length(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with a single underscore ("-").
    
    After the replacement, check if the length of the new string is a prime number. 
    Return True if it is a prime number, False otherwise. 

    prime_underscored_length("Example") == True
    prime_underscored_length("Example 1") == False
    prime_underscored_length(" Example 2") == False
    prime_underscored_length(" Example   3") == False
    prime_underscored_length(" Example    4") == False
    """
    text = re.sub('\\s{2,}', '_', text)
    text = text.replace(' ', '_')
    return is_prime(len(text))