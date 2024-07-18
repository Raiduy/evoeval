def transform_dict(input_dict):
    if not input_dict or not all((isinstance(key, str) for key in input_dict.keys())):
        return {}
    if not all((key.islower() or key.isupper() for key in input_dict.keys())):
        return {}
    result_dict = {}
    for (key, value) in input_dict.items():
        try:
            num = float(value)
            rounded_num = int(num + 0.5) if num > 0 else int(num - 0.5)
            result_dict[key] = rounded_num
        except ValueError:
            return {}
    return result_dict