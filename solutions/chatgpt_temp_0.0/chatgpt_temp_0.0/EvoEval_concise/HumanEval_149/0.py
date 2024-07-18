
def sorted_list_sum(lst):
    """This function takes a list of strings, removes strings with odd lengths,
    and returns the sorted list. Sorting is done primarily according to string length 
    in ascending order, and secondarily alphabetically for strings of the same length. 
    The list may contain duplicates.

    Example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst = [s for s in lst if len(s) % 2 == 0]
    lst.sort(key=lambda s: (len(s), s))
    return lst