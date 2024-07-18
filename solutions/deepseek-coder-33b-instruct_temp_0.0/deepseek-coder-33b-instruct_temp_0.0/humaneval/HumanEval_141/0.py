
def file_name_check(file_name):
    # Check if the file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'

    # Split the file's name into two parts: before and after the dot
    name, extension = file_name.rsplit('.', 1)

    # Check if the substring before the dot is not empty and starts with a letter
    if not re.match(r'^[a-zA-Z]', name):
        return 'No'

    # Check if the substring after the dot is one of ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    # Check if there are not more than three digits in the file's name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'
