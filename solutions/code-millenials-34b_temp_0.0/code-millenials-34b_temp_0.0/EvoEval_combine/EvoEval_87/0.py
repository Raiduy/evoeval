
def match_and_remove_unbalanced(text):
    vowels = 'aeiou'
    stack = []
    balanced = True
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                balanced = False
            else:
                stack.pop()
        elif char in vowels:
            if not balanced:
                text = text.replace(char, '')
    return ''.join(stack) + text if balanced else ''.join(stack) + text.replace('(', '').replace(')', '')