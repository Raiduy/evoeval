
def words_in_sentence(sentence):
    """
    Returns a string of words from the original sentence whose lengths are prime numbers.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words where the length is a prime number
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    # Join the filtered words back into a string
    return ' '.join(prime_length_words)
