
def exchange(lst1, lst2):
    even_count = 0
    odd_count = 0
    for num1 in lst1:
        if num1 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    for num2 in lst2:
        if num2 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count > even_count:
        return 'NO'
    else:
        return 'YES'