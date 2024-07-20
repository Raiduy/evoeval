
def is_nested(string):
    """
    This function takes a string consisting solely of square brackets. It returns True if there is a valid 
    sequence of nested brackets in the string, otherwise it returns False.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
    return len(stack) == 0