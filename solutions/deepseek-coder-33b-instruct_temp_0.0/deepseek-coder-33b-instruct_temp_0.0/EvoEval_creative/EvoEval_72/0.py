def string_fairy_tale(lst):
    fairy_tales = []
    for string in lst:
        name = ''.join(filter(str.isalpha, string))
        count = sum((c.isdigit() for c in string))
        fairy_tale = f"Once upon a time, in a kingdom far away, lived a magical creature with the name of '{name}' who was known for telling {count} tales a day"
        fairy_tales.append(fairy_tale)
    return fairy_tales