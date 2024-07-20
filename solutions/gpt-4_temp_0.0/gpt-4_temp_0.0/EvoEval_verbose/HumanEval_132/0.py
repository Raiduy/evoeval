
def is_nested(string):
    """
    This function is designed to examine a string of square brackets, and determine if the brackets form a valid nested sequence. 
    
    The 'is_nested' function accepts one argument, a string of square brackets. A bracket is considered nested if it is enclosed within another pair of brackets. This function does not consider brackets that are simply adjacent to each other as nested. The function returns a boolean value, where 'True' indicates a valid nested sequence of brackets exists within the input string, and 'False' indicates otherwise.
    
    The function only accepts strings containing square brackets. Any other characters in the input string will result in undefined behaviour. The function does not differentiate between opening and closing brackets, meaning the sequence '[[' is considered valid, but the sequence '][' is not.

    Here are some examples to illustrate the expected input and output:

    Example 1: 
    Input: '[[]]'
    Output: True
    Explanation: The inner pair of brackets is nested within the outer pair.

    Example 2: 
    Input: '[]]]]]]][[[[[]'
    Output: False
    Explanation: No bracket is nested within another.

    Example 3: 
    Input: '[][]'
    Output: False
    Explanation: The pairs of brackets are adjacent, but not nested.

    Example 4:
    Input: '[]'
    Output: False
    Explanation: The brackets are adjacent, but not nested.

    Example 5:
    Input: '[[][]]'
    Output: True
    Explanation: The first pair of inner brackets is nested within the outer pair.

    Example 6:
    Input: '[[]][['
    Output: True
    Explanation: The first pair of brackets is nested within the second pair.
    """
    open_brackets = 0
    for char in string:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            open_brackets -= 1
        if open_brackets < 0:
            return False
    return open_brackets > 1