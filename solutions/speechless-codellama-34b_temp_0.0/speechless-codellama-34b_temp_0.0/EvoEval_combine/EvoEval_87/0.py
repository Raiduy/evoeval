
def match_and_remove_unbalanced(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    stack = []
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return ''.join([c for c in text if c not in vowels])
            stack.pop()
    if stack:
        return ''.join([c for c in text if c not in vowels])
    return text