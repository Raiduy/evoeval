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
    """ html is a string of HTML tags.
    return True if every opening tag has a corresponding closing tag 
    and they are correctly nested. Ignore self-closing tags. 
    The HTML tags are simplified to just the tag names enclosed in "<>" for opening tags and "</>" for closing tags.

    >>> is_valid_html("<html>")
    False
    >>> is_valid_html("<html></html>")
    True
    >>> is_valid_html("<html><body></body></html>")
    True
    >>> is_valid_html("<html><body></html></body>")
    False
    >>> is_valid_html("<html><head></head><body><div></div></body></html>")
    True
    >>> is_valid_html("<html><head></head><body><div></body></div></html>")
    False
    """
    stack = []
    while html:
        (tag, html) = get_next_tag(html)
        if not tag:
            break
        if is_closing_tag(tag):
            if not stack or get_tag_name(stack[-1]) != get_tag_name(tag):
                return False
            stack.pop()
        else:
            stack.append(tag)
    return not stack