
def words_in_sentence(sentence):
    """
    Given a sentence as a string, return a string of words from the input sentence that have prime number lengths. 
    Keep the order of words intact. Each word is separated by a space. 
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)