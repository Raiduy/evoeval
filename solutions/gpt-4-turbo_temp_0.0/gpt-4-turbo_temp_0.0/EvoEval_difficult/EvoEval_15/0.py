def string_sequence_modified(n: int, m: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 up to n inclusive, but replace every m-th number with "Fizz".
    Assume 1-based indexing for m-th number.
    """
    sequence = []
    for i in range(n + 1):
        if (i + 1) % m == 0:
            sequence.append('Fizz')
        else:
            sequence.append(str(i))
    return ' '.join(sequence)