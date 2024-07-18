def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    (i, j) = (0, len(s) - 1)
    arr = list(s)
    while i < j:
        if arr[i] not in vowels:
            i += 1
        elif arr[j] not in vowels:
            j -= 1
        else:
            (arr[i], arr[j]) = (arr[j], arr[i])
            (i, j) = (i + 1, j - 1)
    return ''.join(arr)