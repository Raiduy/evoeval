
def fix_spaces(text):
    # First, replace more than 2 consecutive spaces with a dash
    text = re.sub(r' {3,}', '-', text)
    # Then, replace any remaining spaces with underscores
    text = text.replace(' ', '_')
    return text
