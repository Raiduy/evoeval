def string_fairy_tale(lst):
    tales = []
    for string in lst:
        count = sum((1 for char in string if char.isdigit()))
        tale = "Once upon a time, in a kingdom far away, lived a magical creature with the name of '{}' who was known for telling {} tales a day".format(string, count)
        tales.append(tale)
    return tales