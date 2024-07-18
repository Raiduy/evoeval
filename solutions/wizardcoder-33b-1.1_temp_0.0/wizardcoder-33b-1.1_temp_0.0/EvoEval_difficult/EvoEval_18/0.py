def how_many_times(string: str, substrings: list) -> dict:
    if any((sub == '' for sub in substrings)):
        return 'Substrings cannot be empty'
    counts = {sub: 0 for sub in substrings}
    for sub in substrings:
        start = 0
        while start < len(string):
            pos = string.find(sub, start)
            if pos != -1:
                counts[sub] += 1
                start = pos + 1
            else:
                break
    return counts