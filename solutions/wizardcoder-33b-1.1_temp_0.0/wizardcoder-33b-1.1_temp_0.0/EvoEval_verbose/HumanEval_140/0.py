
def fix_spaces(text):
    text = text.replace(' ', '_')
    text = re.sub('_+', '-', text)
    if text[0] == '_':
        text = '-' + text[1:]
    return text