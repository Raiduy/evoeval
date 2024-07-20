
def search(lst):
    """
    Given a non-empty list of positive integers, return the highest integer that exceeds zero, whose frequency in the list is at least equal to its value. If no such integer exists, return -1.
    The frequency of an integer is its count in the list.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[0], reverse=True))
    for (num, freq) in sorted_dict.items():
        if freq >= num:
            return num
    return -1