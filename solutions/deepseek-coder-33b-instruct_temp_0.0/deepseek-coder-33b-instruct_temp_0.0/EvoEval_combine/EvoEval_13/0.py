def filter_exchange(arr, lst1):
    arr = [num for num in arr if sum((int(digit) for digit in str(abs(num)))) > 0]
    even_count = sum((1 for num in lst1 if num % 2 == 0))
    odd_count = sum((1 for num in arr if num % 2 != 0))
    return 'YES' if even_count >= odd_count else 'NO'