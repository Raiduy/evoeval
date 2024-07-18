
def total_match(lst1, lst2):
    """
    A function that takes two lists of strings as input. It returns the list with the fewer total characters across all its strings. 
    If both lists have the same total number of characters, it returns the first list.

    Examples
    total_match([], []) -> []
    total_match(['hi', 'admin'], ['hI', 'Hi']) -> ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) -> ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) -> ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) -> ['4']
    """
    total_chars_lst1 = sum((len(s) for s in lst1))
    total_chars_lst2 = sum((len(s) for s in lst2))
    if total_chars_lst1 <= total_chars_lst2:
        return lst1
    else:
        return lst2