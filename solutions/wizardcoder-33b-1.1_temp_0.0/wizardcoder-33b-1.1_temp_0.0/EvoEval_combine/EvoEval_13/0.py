def filter_exchange(arr, lst1):
    arr = [num for num in arr if sum((int(digit) for digit in str(abs(num)))) > 0]
    for num in arr:
        if num % 2 != 0 and len(lst1) > 0:
            lst1.remove(num)
    return 'YES' if all((num % 2 == 0 for num in lst1)) else 'NO'