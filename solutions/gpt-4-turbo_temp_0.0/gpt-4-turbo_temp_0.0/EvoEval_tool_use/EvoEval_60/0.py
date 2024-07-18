def get_next_tag(html: str):
    """Extract the next tag from the HTML string.

    Returns a tuple containing the tag (including the brackets) and the rest of the HTML string.
    If no more tags are found, return (None, html).
    """
    start = html.find('<')
    end = html.find('>', start)
    if start == -1 or end == -1:
        return None, html
    return html[start:end+1], html[end+1:]

def is_closing_tag(tag: str):
    """Check if the given tag is a closing tag.
    """
    return tag.startswith('</')

def get_tag_name(tag: str):
    """Extract the name of the tag, without the brackets and the slash for closing tags.
    """
    if is_closing_tag(tag):
        return tag[2:-1]
    return tag[1:-1]
def is_valid_html(html: str):
    """Check if the HTML string has correctly nested and matched tags."""
    stack = []
    current_pos = 0
    while current_pos < len(html):
        (tag, rest) = get_next_tag(html[current_pos:])
        if tag is None:
            break
        if not is_closing_tag(tag):
            stack.append(get_tag_name(tag))
        else:
            if not stack or stack[-1] != get_tag_name(tag):
                return False
            stack.pop()
        current_pos += len(tag) + len(rest) - len(html[current_pos:])
    return not stack