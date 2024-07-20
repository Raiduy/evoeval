def parse_to_list(string):
    """Parse a string of comma-separated numbers into a list of integers. 
    Assume the input string is always valid.
    Example:
    parse_to_list("1,2,3") should return [1,2,3].
    parse_to_list("10,20,30,40") should return [10,20,30,40].
    """
    return [int(i) for i in string.split(",")]
def find_special_triplet(numbers_string):
    """Complete the function that takes in a string of comma-separated integers and returns the first "special" triplet from the list if it exists. A "special" triplet is a sequence of three numbers (x, y, z) that appear consecutively in the list, such that x < y and y < z. If no such triplet exists, the function should return an empty list. Return the first triplet in the order of appearance in the list
    Assume the input string is always valid and each number in the string is an integer between 1 and 100 (both inclusive).

    Examples:
    find_special_triplet("1,2,3,4") should return [1,2,3].
    find_special_triplet("10,20,30,40") should return [10,20,30].
    find_special_triplet("100,99,98") should return [].
    """
    numbers_list = parse_to_list(numbers_string)
    for i in range(len(numbers_list) - 2):
        if numbers_list[i] < numbers_list[i + 1] and numbers_list[i + 1] < numbers_list[i + 2]:
            return numbers_list[i:i + 3]
    return []