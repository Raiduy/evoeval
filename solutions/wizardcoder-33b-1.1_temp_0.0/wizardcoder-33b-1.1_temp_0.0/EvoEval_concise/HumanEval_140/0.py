
def fix_spaces(text):
    text = text.replace(' ', '_')
    text = re.sub('_+', '-', text)
    return text