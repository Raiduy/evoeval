
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if len(name) == 0 or not name[0].isalpha():
        return 'No'
    
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
