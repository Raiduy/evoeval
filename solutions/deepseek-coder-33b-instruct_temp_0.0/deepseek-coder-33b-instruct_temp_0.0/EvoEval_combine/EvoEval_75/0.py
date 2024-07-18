def transform_dict(input_dict):
    if not input_dict or not all((isinstance(k, str) for k in input_dict.keys())):
        return {}
    if not all((k.isupper() for k in input_dict.keys())) and (not all((k.islower() for k in input_dict.keys()))):
        return {}
    return {k: round(float(v)) for (k, v) in input_dict.items()}