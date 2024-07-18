def transform_dict(input_dict):
    if not input_dict or not all((isinstance(key, str) for key in input_dict.keys())):
        return {}
    if not all((key.isupper() or key.islower() for key in input_dict.keys())):
        return {}
    result = {}
    for (key, value) in input_dict.items():
        try:
            num = float(value)
            if num >= 0:
                result[key] = int(num + 0.5)
            else:
                result[key] = int(num - 0.5)
        except ValueError:
            return {}
    return result