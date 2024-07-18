
def correct_bracket_sequence_and_count(string: str, bracket: str) -> tuple:
    count = string.count(bracket)
    if bracket == '<':
        return (string.count('<') == string.count('>'), count)
    else:
        return (string.count('<') == string.count('>'), count)