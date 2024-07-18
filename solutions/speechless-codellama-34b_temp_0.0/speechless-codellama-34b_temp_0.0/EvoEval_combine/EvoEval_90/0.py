
def vowels_in_dict_keys(dictionary):
    vowels = set('aeiouAEIOU')
    result = {}
    for key in dictionary:
        if not isinstance(key, str):
            return {}
        if any((c.islower() and c.isupper() for c in key)):
            return {}
        if all((c.islower() for c in key)) or all((c.isupper() for c in key)):
            result[key] = sum((1 for c in key if c in vowels))
            if key.endswith('y'):
                result[key] -= 1
    return result