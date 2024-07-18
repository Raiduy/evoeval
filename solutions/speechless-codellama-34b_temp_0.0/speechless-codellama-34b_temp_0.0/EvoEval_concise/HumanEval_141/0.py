
def file_name_check(file_name):
    if len(file_name) > 3 and file_name[:4].isdigit():
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not file_name[0].isalpha() or file_name.index('.') == 0:
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'