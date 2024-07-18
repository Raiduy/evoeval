
def words_string(s):
    if ',' in s:
        return s.split(',')
    else:
        return s.split()
