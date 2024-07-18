
def exchange(lst1, lst2):
    odd_count = sum((1 for num in lst1 if num % 2 != 0))
    even_count = sum((1 for num in lst2 if num % 2 == 0))
    if odd_count <= even_count:
        return 'YES'
    else:
        return 'NO'