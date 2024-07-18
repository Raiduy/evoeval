def smallest_change(arr, k):

    def is_palindromic(arr):
        return arr == arr[::-1]

    def sum_divisible_by_k(arr, k):
        return sum(arr) % k == 0
    if is_palindromic(arr) and sum_divisible_by_k(arr, k):
        return 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[j] = arr[i]
            if is_palindromic(arr) and sum_divisible_by_k(arr, k):
                return j - i
            arr[j] = arr[j]
    return len(arr)