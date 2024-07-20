
def match_and_remove_unbalanced(text):
    """
    This function takes a string as an input. The string consists of parentheses '(',')' and alphabets only.
    The task is to check if the parentheses in the string are balanced and if unbalanced, remove the vowels from the string.
    Return the same string if the parentheses are balanced.
    The parentheses are considered balanced if every open parenthesis has a corresponding close parenthesis. 

    Examples:
    match_and_remove_unbalanced('a(b)c(def)') == 'a(b)c(def)'
    match_and_remove_unbalanced('a(bc)de(fg') == '(bc)d(fg'
    match_and_remove_unbalanced('ab)c(de)f') == 'b)c(d)f'
    match_and_remove_unbalanced('ab(cd') == 'b(cd'
    """
    stack = []
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    if stack:
        return ''.join([char for char in text if char.lower() not in 'aeiou'])
    else:
        return text