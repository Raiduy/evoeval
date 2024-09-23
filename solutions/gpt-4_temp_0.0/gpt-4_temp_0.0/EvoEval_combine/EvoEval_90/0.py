
def vowels_in_dict_keys(dict):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = {}
    keys = list(dict.keys())
    if not all((isinstance(key, str) for key in keys)):
        return {}
    if not (all((key.islower() for key in keys)) or all((key.isupper() for key in keys))):
        return {}
    for key in keys:
        count = sum((1 for char in key if char.lower() in vowels))
        if key.endswith('y') or key.endswith('Y'):
            count += 1
        result[key] = count
    return result