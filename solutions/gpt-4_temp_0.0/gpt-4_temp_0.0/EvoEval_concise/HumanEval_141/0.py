
def file_name_check(file_name):
    """
    Checks a file name's validity based on specific conditions, and returns 'Yes' if valid and 'No' if not valid. The conditions are as follows:
    - No more than three digits ('0'-'9') in the file name.
    - Exactly one dot '.' in the file name.
    - The substring before the dot should begin with a latin alphabet letter ('a'-'z' or 'A'-'Z') and should not be empty.
    - The substring after the dot should be 'txt', 'exe', or 'dll'.
    
    Example:
    file_name_check("example.txt") returns 'Yes'
    file_name_check("1example.dll") returns 'No' (file name doesn't start with a latin alphabet letter)
    """
    if file_name.count('.') != 1:
        return 'No'
    (name, extension) = file_name.split('.')
    if not name[0].isalpha() or sum((c.isdigit() for c in name)) > 3:
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'