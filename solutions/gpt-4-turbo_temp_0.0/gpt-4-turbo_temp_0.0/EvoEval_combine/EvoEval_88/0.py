
def process_and_sort_string(s):
    words = s.replace(',', ' ').split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    sorted_words = sorted(even_length_words, key=lambda word: (len(word), word))
    return sorted_words