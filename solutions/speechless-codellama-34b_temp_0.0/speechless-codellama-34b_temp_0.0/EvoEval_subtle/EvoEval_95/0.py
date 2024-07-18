
def check_dict_case(dictionary):
    if len(dictionary) < 3 or not dictionary:
        return False
    lower_case = all((isinstance(key, str) and key.islower() for key in dictionary.keys()))
    upper_case = all((isinstance(key, str) and key.isupper() for key in dictionary.keys()))
    return lower_case or upper_case