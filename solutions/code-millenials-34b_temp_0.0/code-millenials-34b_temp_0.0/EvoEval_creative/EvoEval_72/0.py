def string_fairy_tale(lst):
    result = []
    for (i, s) in enumerate(lst):
        name = s.split('1234567890')[0]
        digit_count = sum((c.isdigit() for c in s))
        story = "Once upon a time, in a kingdom far away, lived a magical creature with the name of '{0}' who was known for telling {1} tales a day".format(s, digit_count)
        result.append(story)
    return result