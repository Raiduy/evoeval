def string_fairy_tale(lst):
    """Given a list of strings, where each string consists of a mix of letters and numbers, return a list.
    Each element of the output should be a fairy tale inspired story. The story should be "Once upon a time, 
    in a kingdom far away, lived a magical creature with the name of 'i' who was known for telling 'j' tales a day,
    where 'i' is the i'th string of the input and 'j' is the count of digits in that string.
    """
    result = []
    for i in lst:
        count = sum((c.isdigit() for c in i))
        result.append(f"Once upon a time, in a kingdom far away, lived a magical creature with the name of '{i}' who was known for telling {count} tales a day")
    return result