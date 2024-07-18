
def vowels_in_dict_keys(dict):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = {}
    for key in dict.keys():
        if not isinstance(key, str):
            return {}
        if not key.islower() and (not key.isupper()):
            return {}
        count = 0
        for char in key:
            if char.lower() in vowels:
                count += 1
        result[key] = count
    return result