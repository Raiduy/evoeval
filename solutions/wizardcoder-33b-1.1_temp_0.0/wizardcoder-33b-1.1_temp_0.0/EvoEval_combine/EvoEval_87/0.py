
def match_and_remove_unbalanced(text):
    stack = []
    vowels = 'aeiou'
    result = ''
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += char
        elif not stack:
            result += char
    if stack:
        result = ''.join([char for char in result if char.lower() not in vowels])
    return result