def how_many_times(string: str, substrings: list) -> dict:
    if not substrings:
        return 'Substrings cannot be empty'
    if string == '':
        return {substring: 0 for substring in substrings}
    counts = {substring: string.count(substring) for substring in substrings}
    return counts