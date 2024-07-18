
def is_nested(string):
    # Initialize a counter for open brackets
    open_brackets = 0
    # Initialize a flag to check if there's a nested bracket
    nested = False

    # Iterate through each character in the string
    for char in string:
        # If it's an opening bracket, increment the counter
        if char == '[':
            open_brackets += 1
        # If it's a closing bracket
        elif char == ']':
            # Decrement the counter because a pair is completed
            open_brackets -= 1
            # If after decrementing, open_brackets is still positive,
            # it means there's a nested structure
            if open_brackets > 0:
                nested = True
        # If open_brackets goes negative, it means there are more closing brackets
        # than opening ones, which is invalid. Break early.
        if open_brackets < 0:
            break

    # Return True if nested structure is found and there are no unmatched brackets
    return nested and open_brackets == 0
