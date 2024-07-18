
def vowels_in_dict_keys(input_dict):
    if not input_dict:
        return {}
    if all((isinstance(key, str) for key in input_dict.keys())):
        if not (all((key.islower() for key in input_dict.keys())) or all((key.isupper() for key in input_dict.keys()))):
            return {}
    else:
        return {}

    def count_vowels(key):
        vowels = 'aeiou'
        count = sum((1 for char in key if char.lower() in vowels))
        if key.endswith('y') or key.endswith('Y'):
            count += 1
        return count
    result_dict = {key: count_vowels(key) for key in input_dict.keys()}
    return result_dict