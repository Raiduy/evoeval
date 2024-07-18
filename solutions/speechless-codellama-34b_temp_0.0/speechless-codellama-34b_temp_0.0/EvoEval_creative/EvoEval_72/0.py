def string_fairy_tale(lst):
    result = []
    for (i, string) in enumerate(lst):
        count = sum((c.isdigit() for c in string))
        story = f"Once upon a time, in a kingdom far away, lived a magical creature with the name of '{string}' who was known for telling {count} tales a day"
        result.append(story)
    return result