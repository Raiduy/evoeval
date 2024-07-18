
def file_name_check(file_name):
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into the name part and the extension part
    name_part, extension_part = file_name.split('.')
    
    # Check if the name part is not empty and starts with a latin alphabet letter
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check if the extension part is one of the allowed extensions
    if extension_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check if there are no more than three digits in the file name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # If all checks passed, return 'Yes'
    return 'Yes'
