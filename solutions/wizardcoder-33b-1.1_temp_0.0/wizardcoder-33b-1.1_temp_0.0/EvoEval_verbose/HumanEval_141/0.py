
def file_name_check(file_name):
    if len(re.findall('\\d', file_name)) > 3:
        return 'No'
    (name, extension) = file_name.split('.')
    if not name[0].isalpha() or extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'