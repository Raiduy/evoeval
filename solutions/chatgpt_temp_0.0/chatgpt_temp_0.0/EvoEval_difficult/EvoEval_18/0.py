def how_many_times(string: str, substrings: list) -> dict:
    if any((sub == '' for sub in substrings)):
        return 'Substrings cannot be empty'
    if string == '':
        return {sub: 0 for sub in substrings}
    counts = {}
    for sub in substrings:
        count = 0
        start = 0
        while start < len(string):
            index = string.find(sub, start)
            if index == -1:
                break
            count += 1
            start = index + 1
        counts[sub] = count
    return counts