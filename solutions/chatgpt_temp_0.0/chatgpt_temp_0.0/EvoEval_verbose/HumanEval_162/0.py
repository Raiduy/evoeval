
def string_to_md5(text):
    if text == '':
        return None
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash