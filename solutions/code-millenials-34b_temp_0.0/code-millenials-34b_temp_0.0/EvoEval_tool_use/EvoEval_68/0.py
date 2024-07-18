def extract_numbers(sentence):
    """
    A helper function that extracts all the numbers in a sentence and return them as a list
    This function uses regex to achieve this.
    Args:
        sentence (str): A sentence which contains numbers.
    Returns:
        list of int: A list of numbers found in the sentence.
    """
    import re
    numbers = re.findall(r'\d+', sentence)
    return [int(i) for i in numbers]
def zoo_animal_distribution(s, n):
    numbers = extract_numbers(s)
    lions = numbers[0]
    tigers = numbers[1]
    elephants = n - lions - tigers
    return elephants