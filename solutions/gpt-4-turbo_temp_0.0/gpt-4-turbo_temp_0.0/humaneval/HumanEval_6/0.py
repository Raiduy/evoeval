from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups based on spaces
    groups = paren_string.split()
    # Initialize an empty list to store the maximum depth of each group
    max_depths = []

    # Iterate through each group
    for group in groups:
        # Initialize counters for the current depth and maximum depth
        current_depth = 0
        max_depth = 0
        # Iterate through each character in the group
        for char in group:
            if char == '(':
                # Increase the current depth for an opening parenthesis
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Decrease the current depth for a closing parenthesis
                current_depth -= 1
        # Add the maximum depth of the current group to the list
        max_depths.append(max_depth)

    return max_depths
