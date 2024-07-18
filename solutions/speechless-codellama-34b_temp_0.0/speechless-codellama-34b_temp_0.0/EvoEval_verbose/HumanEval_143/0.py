
def words_in_sentence(sentence):
    """
    This function accepts a single input, which is a string that represents a sentence. Each individual word 
    in the sentence is separated by a space. Your job is to return a string that includes only the words from 
    the original sentence that have a length that is a prime number. Prime numbers are integers greater than 1 
    that have no divisors other than 1 and themselves. The words in the returned string should appear in the 
    same order as they do in the original sentence. 
    """
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)