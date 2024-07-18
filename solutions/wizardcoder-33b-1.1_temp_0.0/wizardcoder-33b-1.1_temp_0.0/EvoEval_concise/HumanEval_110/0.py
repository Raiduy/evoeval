
def exchange(lst1, lst2):
    if all((num % 2 == 0 for num in lst1)):
        return 'YES'
    for num1 in lst1:
        if num1 % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    return 'YES'
    return 'NO'