
def fix_spaces(text):
    text = re.sub(' {2,}', '-', text)
    text = text.replace(' ', '_')
    return text