
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
    digits_count = 0
    dot_count = 0
    latin_letter_found = False
    file_extension = ''
    for char in file_name:
        if char.isdigit():
            digits_count += 1
        elif char == '.':
            dot_count += 1
        elif char.isalpha() and (not latin_letter_found):
            latin_letter_found = True
        elif dot_count == 1:
            file_extension += char
    if digits_count <= 3 and dot_count == 1 and latin_letter_found and (file_extension in ['txt', 'exe', 'dll']):
        return 'Yes'
    else:
        return 'No'