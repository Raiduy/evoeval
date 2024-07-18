
def anti_shuffle(s):
    parts = re.findall('\\b\\w+\\b|[^\\w\\s]|\\s+', s)
    sorted_parts = [''.join(sorted(part)) if part.isalpha() else part for part in parts]
    return ''.join(sorted_parts)