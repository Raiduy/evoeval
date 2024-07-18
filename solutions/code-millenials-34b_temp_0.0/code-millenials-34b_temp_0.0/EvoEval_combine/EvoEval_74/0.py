def sum_exchange(lst1, lst2, x, y, z):
    answer = ''
    for num in lst1:
        if num % 2 != 0:
            if num in lst2:
                lst1.remove(num)
                lst2.remove(num)
                lst1.append(num)
            else:
                answer = 'NO'
                break
    if x == y + z or x == z + y or y == x + z or (y == z + x) or (z == x + y) or (z == y + x):
        answer = 'SUM ' + answer
    else:
        answer = 'NO_SUM ' + answer
    return answer