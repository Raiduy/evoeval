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
    """
    In this task, you will be given a string that represents the number of lions and tigers that are distributed in a zoo, and a number that represents the total number of animals in the zoo.
    Return the number of elephants in the zoo. Note that the zoo only contains lions, tigers,
    and elephants.
    The string given will be in the form "There are {number} lions and {number} tigers in the zoo"

    for example:
    zoo_animal_distribution("There are 5 lions and 6 tigers in the zoo", 19) -> 19 - 5 - 6 = 8
    zoo_animal_distribution("There are 0 lions and 1 tigers in the zoo", 3) -> 3 - 0 - 1 = 2
    zoo_animal_distribution("There are 2 lions and 3 tigers in the zoo", 100) -> 100 - 2 - 3 = 95
    zoo_animal_distribution("There are 100 lions and 1 tigers in the zoo", 120) -> 120 - 100 - 1 = 19
    """
    numbers = extract_numbers(s)
    return n - sum(numbers)