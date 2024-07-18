def transform_dict(input_dict):
    if not input_dict or not all((isinstance(k, str) for k in input_dict.keys())):
        return {}
    keys_case = 'lower' if all((k.islower() for k in input_dict.keys())) else 'upper'
    if keys_case is None:
        return {}
    new_dict = {}
    for (k, v) in input_dict.items():
        try:
            num = float(v)
            new_dict[k] = round(num)
        except ValueError:
            return {}
    return new_dict