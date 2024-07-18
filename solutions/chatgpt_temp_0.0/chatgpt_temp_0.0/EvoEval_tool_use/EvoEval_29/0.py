from typing import List, Tuple

def get_words(text: str) -> List[str]:
    """Split the input text into words.
    The words in the returned list should not contain any punctuation or special characters.
    Each word should be in lower case.
    >>> get_words('Hello, World!')
    ['hello', 'world']
    """
    import re
    words = re.sub('[^A-Za-z0-9 ]+', '', text).lower().split()
    return words


def count_frequency(words: List[str]) -> dict:
    """Count the frequency of each word in the list.
    Return a dictionary where keys are words and values are their frequency.
    >>> count_frequency(['hello', 'world', 'hello'])
    {'hello': 2, 'world': 1}
    """
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict
from typing import List, Tuple

def top_k_frequent_words(text: str, k: int) -> List[Tuple[str, int]]:
    """
    Given a string of words and an integer k, return a list of k most frequent words and their frequencies in the text.
    Words should be compared in case insensitive manner and the list should be sorted in descending order of frequency.
    In case of frequency tie, words should be sorted in lexicographic order.
    If k is greater than number of unique words, return all words and their frequencies.
    Words in string can be separated by spaces and can contain punctuation/special characters which should be ignored.
    The frequencies should be calculated after removing punctuation and converting words to lowercase.

    >>> top_k_frequent_words('Hello, World! Hello, Python. Python, Python!', 2)
    [('python', 3), ('hello', 2)]
    """
    words = get_words(text)
    freq_dict = count_frequency(words)
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq[:k]