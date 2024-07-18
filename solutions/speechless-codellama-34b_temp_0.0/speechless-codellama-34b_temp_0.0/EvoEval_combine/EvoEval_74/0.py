def sum_exchange(lst1, lst2, x, y, z):
    even_lst1 = [num for num in lst1 if num % 2 == 0]
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    if len(even_lst1) == len(lst1):
        answer = 'YES'
    elif len(odd_lst1) == len(lst1):
        answer = 'NO'
    else:
        answer = 'YES' if len(even_lst1) + len(odd_lst2) == len(lst1) else 'NO'
    if x + y == z or x + z == y or y + z == x:
        answer = 'SUM ' + answer
    else:
        answer = 'NO_SUM ' + answer
    return answer