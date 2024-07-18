
def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]

    # Initialize a counter for open parentheses
    count = 0

    # Iterate over the characters in the string
    for c in s:
        if c == '(':
            # If the character is an open parenthesis, increment the counter
            count += 1
        elif c == ')':
            # If the character is a close parenthesis, decrement the counter
            count -= 1

        # If the counter goes negative, it means we have more close parentheses
        # than open parentheses, so the string is not good
        if count < 0:
            return 'No'

    # If the counter is not zero, it means we have more open parentheses
    # than close parentheses, so the string is not good
    if count != 0:
        return 'No'

    # If we have not returned 'No' yet, the string is good
    return 'Yes'
