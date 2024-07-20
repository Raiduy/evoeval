
def fix_spaces(text):
    """
    Replaces all spaces in the input string 'text' with underscores. If 'text' contains 
    more than two consecutive spaces, these are replaced with a single dash. 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = re.sub(' {3,}', '-', text)
    text = re.sub(' ', '_', text)
    return text