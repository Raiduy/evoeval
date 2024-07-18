
def check_dict_case(dict):
    if len(dict) == 0:
        return False

    keys = list(dict.keys())
    first_key = keys[0]
    is_lower = first_key.islower()
    is_upper = first_key.isupper()

    for key in keys:
        if (is_lower and not key.islower()) or (is_upper and not key.isupper()):
            return False

    return True
