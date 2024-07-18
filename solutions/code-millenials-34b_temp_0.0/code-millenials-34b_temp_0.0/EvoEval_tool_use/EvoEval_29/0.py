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
    words = get_words(text)
    freq_dict = count_frequency(words)
    sorted_words = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]