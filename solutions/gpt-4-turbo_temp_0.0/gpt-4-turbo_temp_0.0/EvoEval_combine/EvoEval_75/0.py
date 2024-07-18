def transform_dict(input_dict):
    if not input_dict:
        return {}
    if not all((isinstance(key, str) for key in input_dict.keys())) or not (all((key.isupper() for key in input_dict)) or all((key.islower() for key in input_dict))):
        return {}
    output_dict = {}
    for (key, value) in input_dict.items():
        try:
            num = float(value)
            if num > 0:
                rounded_num = int(num + 0.5)
            else:
                rounded_num = int(num - 0.5)
            output_dict[key] = rounded_num
        except ValueError:
            return {}
    return output_dict