
def file_name_check(file_name):
    # Check if there are more than three digits in the file name
    if len(file_name) > 3 and file_name[:4].isdigit():
        return 'No'
    
    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    # Check if the substring before the dot is not empty and starts with a latin alphapet letter
    if not file_name[0].isalpha() or file_name[0].isdigit():
        return 'No'
    
    # Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'
