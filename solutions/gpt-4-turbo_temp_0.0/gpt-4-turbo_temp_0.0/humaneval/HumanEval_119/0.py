
def match_parens(lst):
    # Count the number of opening and closing parentheses in both strings
    open_close_counts = [(s.count('('), s.count(')')) for s in lst]
    
    # Check if either string has more closing parentheses than the other has opening parentheses
    if open_close_counts[0][1] > open_close_counts[1][0] or open_close_counts[1][1] > open_close_counts[0][0]:
        return 'No'
    
    # If we reach this point, it means it's possible to form a balanced string
    return 'Yes'
