
def fix_spaces(text):
    """
    Replaces all spaces in the input string 'text' with underscores. If 'text' contains 
    more than two consecutive spaces, these are replaced with a single dash. 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = []
    i = 0
    while i < len(text):
        if text[i] == ' ':
            if i + 1 < len(text) and text[i + 1] == ' ':
                result.append('-')
                i += 2
                while i < len(text) and text[i] == ' ':
                    i += 1
            else:
                result.append('_')
                i += 1
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)