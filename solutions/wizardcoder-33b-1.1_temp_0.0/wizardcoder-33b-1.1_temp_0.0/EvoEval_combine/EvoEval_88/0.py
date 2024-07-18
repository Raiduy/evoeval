
def process_and_sort_string(s):
    words = s.replace(',', '').split()
    words = [word for word in words if len(word) % 2 == 0]
    words.sort(key=lambda x: (len(x), x))
    return words