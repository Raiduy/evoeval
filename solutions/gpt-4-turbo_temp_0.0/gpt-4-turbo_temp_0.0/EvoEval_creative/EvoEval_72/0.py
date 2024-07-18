def string_fairy_tale(lst):
    """Given a list of strings, where each string consists of a mix of letters and numbers, return a list.
    Each element of the output should be a fairy tale inspired story. The story should be "Once upon a time, 
    in a kingdom far away, lived a magical creature with the name of 'i' who was known for telling 'j' tales a day,
    where 'i' is the i'th string of the input and 'j' is the count of digits in that string.
    """
    fairy_tales = []
    for creature in lst:
        digit_count = sum((c.isdigit() for c in creature))
        story = f"Once upon a time, in a kingdom far away, lived a magical creature with the name of '{creature}' who was known for telling {digit_count} tales a day"
        fairy_tales.append(story)
    return fairy_tales