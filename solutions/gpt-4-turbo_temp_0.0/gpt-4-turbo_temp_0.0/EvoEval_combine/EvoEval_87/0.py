
def match_and_remove_unbalanced(text):
    open_parentheses = 0
    for char in text:
        if char == '(':
            open_parentheses += 1
        elif char == ')':
            if open_parentheses > 0:
                open_parentheses -= 1
            else:
                open_parentheses = -1
                break
    if open_parentheses == 0:
        return text
    else:
        vowels = 'aeiouAEIOU'
        return ''.join([char for char in text if char not in vowels])