def check_dict_case_content(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    values = list(dict.values())
    if not all((isinstance(key, str) for key in keys)) or not all((isinstance(value, str) for value in values)):
        return False
    if len(set((len(key) for key in keys))) > 1:
        return False
    if all((key.islower() for key in keys)):
        return all((value.istitle() for value in values))
    elif all((key.isupper() for key in keys)):
        return all((value.istitle() for value in values))
    else:
        return False