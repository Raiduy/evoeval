
def match_and_remove_unbalanced(text):
    stack = []
    vowels = set('aeiouAEIOU')
    result = []
    for char in text:
        if char == '(':
            stack.append(char)
            result.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                result.append(char)
        else:
            result.append(char)
    if stack:
        result = [char for char in result if char not in vowels]
    return ''.join(result)