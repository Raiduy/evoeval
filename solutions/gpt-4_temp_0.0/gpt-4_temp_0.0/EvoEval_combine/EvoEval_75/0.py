def transform_dict(input_dict):
    """
    Create a function that takes a dictionary as an input where keys are strings and values are strings 
    representing numbers. The function should return a new dictionary where the keys remain the same, 
    but each value is replaced with the closest integer to it. If the number is equidistant from two 
    integers, round it away from zero. The function should return an empty dictionary if keys are not 
    all in upper case or all in lower case.

    The function should also return an empty dictionary if the given dictionary is empty or if keys are not all strings.

    Examples:

    >>> transform_dict({"a":"10", "b":"15.3"})
    {"a": 10, "b": 15}
    >>> transform_dict({"A":"10.5", "B":"-15.5"})
    {"A": 11, "B": -16}
    >>> transform_dict({"a":"10", "B":"15.3"})
    {}
    >>> transform_dict({"a": "10.5", 8: "-15.5"})
    {}

    Note:
    Rounding away from zero means that if the given number is equidistant from two integers, the one 
    you should return is the one that is the farthest from zero. For example, if the value string 
    represents "14.5", it should return 15 and if it represents "-14.5", it should return -15.
    """
    if not input_dict or not all((isinstance(k, str) for k in input_dict.keys())):
        return {}
    if not all((k.isupper() for k in input_dict.keys())) and (not all((k.islower() for k in input_dict.keys()))):
        return {}
    return {k: round(float(v)) if float(v) - int(float(v)) != 0.5 else int(float(v)) + 1 if float(v) > 0 else int(float(v)) - 1 for (k, v) in input_dict.items()}