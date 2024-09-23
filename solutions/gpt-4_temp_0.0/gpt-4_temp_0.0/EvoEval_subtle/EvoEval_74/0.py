
def total_match(lst1, lst2):
    """
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list greater than the other list.

    if the two lists have the same number of chars, return the second list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'hi', 'admin', 'project']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hi', 'admin']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['1', '2', '3', '4', '5']
    """
    total_chars_lst1 = sum((len(word) for word in lst1))
    total_chars_lst2 = sum((len(word) for word in lst2))
    if total_chars_lst1 > total_chars_lst2:
        return lst1
    else:
        return lst2