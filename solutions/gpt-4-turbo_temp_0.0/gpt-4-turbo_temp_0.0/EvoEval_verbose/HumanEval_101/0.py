
def words_string(s):
    words = re.split('[,\\s]\\s*', s)
    words = [word for word in words if word]
    return words