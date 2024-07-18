
def file_name_check(file_name):
    # Check if there are more than three digits in the file's name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Split the file's name into two parts: before and after the dot
    parts = file_name.split('.')

    # Check if there is exactly one dot in the file's name
    if len(parts) != 2:
        return 'No'

    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not re.match(r'^[a-zA-Z]', parts[0]):
        return 'No'

    # Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
