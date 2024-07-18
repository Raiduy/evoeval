
def string_to_md5(text):
    if text == '':
        return None
    else:
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
