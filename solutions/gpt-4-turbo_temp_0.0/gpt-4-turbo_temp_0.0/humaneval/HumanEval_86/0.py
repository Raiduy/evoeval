
def anti_shuffle(s):
    # Split the string into words and non-words (like spaces and punctuation)
    parts = re.findall(r'\b\w+\b|[^\w\s]|\s+', s)
    
    # Sort the characters of each word and keep non-words as they are
    sorted_parts = ["".join(sorted(part)) if part.isalpha() else part for part in parts]
    
    # Join the parts back together
    return "".join(sorted_parts)
