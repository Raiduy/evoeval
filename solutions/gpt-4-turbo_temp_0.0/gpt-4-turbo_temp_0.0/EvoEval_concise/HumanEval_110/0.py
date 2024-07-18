
def exchange(lst1, lst2):
    """Create a function that checks if it's possible to exchange elements between two input lists of numbers,
    lst1 and lst2, to transform lst1 into a list of only even numbers. The exchange of elements is unlimited. 
    If the conversion is feasible, the function returns "YES". If it's not, it returns "NO". 
    The input lists will always be non-empty.
    Example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    """
    even_count_lst1 = sum((1 for x in lst1 if x % 2 == 0))
    even_count_lst2 = sum((1 for x in lst2 if x % 2 == 0))
    odd_count_lst1 = len(lst1) - even_count_lst1
    if odd_count_lst1 == 0 or even_count_lst2 >= odd_count_lst1:
        return 'YES'
    else:
        return 'NO'