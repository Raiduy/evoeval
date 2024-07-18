
def match_and_remove_unbalanced(text):
    stack = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                result += char
        elif char not in vowels:
            result += char
    while len(stack) > 0:
        result += stack.pop()
    return result