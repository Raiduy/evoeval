
def file_name_check(file_name):
    if len(re.findall('\\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not re.match('[a-zA-Z]', file_name.split('.')[0]):
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'