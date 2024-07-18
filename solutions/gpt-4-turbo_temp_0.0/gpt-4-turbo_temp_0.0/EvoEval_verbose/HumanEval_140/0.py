
def fix_spaces(text):
    text = re.sub(' {3,}', '-', text)
    text = text.replace(' ', '_')
    return text