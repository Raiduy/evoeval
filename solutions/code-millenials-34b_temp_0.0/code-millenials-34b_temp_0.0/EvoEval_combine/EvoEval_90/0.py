
def vowels_in_dict_keys(dict):
    vowels = 'aeiou'
    if not dict:
        return {}
    result = {}
    for key in dict:
        if not isinstance(key, str) or (not key.isupper() and (not key.islower())):
            return {}
        count = 0
        for char in key:
            if char in vowels:
                count += 1
        if key[-1] == 'y' or key[-1] == 'Y':
            count += 1
        result[key] = count
    return result