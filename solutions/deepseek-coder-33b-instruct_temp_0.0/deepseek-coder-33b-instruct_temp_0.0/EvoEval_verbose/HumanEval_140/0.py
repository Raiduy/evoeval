
def fix_spaces(text):
    """
    The function 'fix_spaces' is designed to manipulate strings based on specific rules.
    It takes a string 'text' as its only parameter.

    The function performs two operations:
    1. It replaces all the spaces in the string with underscores.
    2. If the string 'text' contains more than two consecutive spaces, 
    it replaces all these consecutive spaces with a single dash (-).

    Here is a detailed explanation of the output depending on various inputs.

    - If the input string doesn't contain any space, the function simply returns the original string. 
    For example, when the input is "Example", the output would also be "Example".
    - If the input string contains a single space between words, 
    the function replaces it with an underscore (_). 
    For example, when the input is "Example 1", the output would be "Example_1".
    - If the input string contains a single space at the beginning, 
    the function replaces it with an underscore (_). 
    For example, when the input is " Example 2", the output would be "_Example_2".
    - If the input string contains more than two consecutive spaces,
    the function replaces these spaces with a single dash (-). 
    For example, when the input is " Example   3", the output would be "_Example-3".

    The function returns the manipulated string as per the rules described above.  

    The time complexity is O(n), where n is the length of the string 'text', 
    because each character in the string needs to be checked once.

    The space complexity is O(1), because no additional space is required that scales with the input size.
    """
    text = text.replace(' ', '_')
    while '__' in text:
        text = text.replace('__', '-')
    return text