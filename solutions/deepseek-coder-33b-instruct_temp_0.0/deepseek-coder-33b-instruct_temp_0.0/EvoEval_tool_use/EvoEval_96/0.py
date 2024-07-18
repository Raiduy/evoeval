def parse_to_list(string):
    """Parse a string of comma-separated numbers into a list of integers. 
    Assume the input string is always valid.
    Example:
    parse_to_list("1,2,3") should return [1,2,3].
    parse_to_list("10,20,30,40") should return [10,20,30,40].
    """
    return [int(i) for i in string.split(",")]
def find_special_triplet(numbers_string):
    numbers = [int(i) for i in numbers_string.split(',')]
    for i in range(len(numbers) - 2):
        if numbers[i] < numbers[i + 1] and numbers[i + 1] < numbers[i + 2]:
            return numbers[i:i + 3]
    return []