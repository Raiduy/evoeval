
def words_in_sentence(sentence):
    """
    Return a string of words from the original sentence whose lengths are prime numbers.
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)