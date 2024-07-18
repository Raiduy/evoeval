
def exchange(lst1, lst2):
    """Create a function that checks if it's possible to exchange elements between two input lists of numbers,
    lst1 and lst2, to transform lst1 into a list of only even numbers. The exchange of elements is unlimited. 
    If the conversion is feasible, the function returns "YES". If it's not, it returns "NO". 
    The input lists will always be non-empty.
    Example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    """
    if all((num % 2 == 0 for num in lst1)):
        return 'YES'
    if any((num % 2 != 0 for num in lst1)) and any((num % 2 == 0 for num in lst2)):
        return 'YES'
    return 'NO'