def filter_exchange(arr, lst1):
    arr = [x for x in arr if sum((int(y) for y in str(abs(x)))) > 0]
    odd_count = 0
    even_count = 0
    for num in lst1:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count >= even_count:
        return 'YES'
    else:
        return 'NO'