def sum_exchange(lst1, lst2, x, y, z):
    """
    In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, the answer is "YES".
    Otherwise, the answer is "NO".
    After that, the function also takes in three more integers, x, y and z.
    It will check if one of these integers is equal to the sum of the other two.
    If this is true, append "SUM" to the front of the answer string.
    Otherwise, append "NO_SUM" to the front of the answer string.
    For example:
    sum_exchange([1, 2, 3, 4], [1, 2, 3, 4], 5, 2, 2) => "NO_SUM YES"
    sum_exchange([1, 2, 3, 4], [1, 5, 3, 4], 4, 2, 2) => "SUM NO"
    It is assumed that the input lists will be non-empty.
    """
    if x == y + z or y == x + z or z == x + y:
        sum_str = 'SUM'
    else:
        sum_str = 'NO_SUM'
    for num in lst1:
        if num % 2 != 0:
            if num in lst2:
                lst2.remove(num)
                lst1.remove(num)
    for num in lst1:
        if num % 2 != 0:
            return sum_str + ' NO'
    return sum_str + ' YES'