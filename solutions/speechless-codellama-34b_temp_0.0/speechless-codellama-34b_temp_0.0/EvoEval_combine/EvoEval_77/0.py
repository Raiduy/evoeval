
def mixed_solution(arr):
    result = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            digits = list(str(arr[i]))
            if any((int(d) > 0 for d in digits)):
                result += arr[i]
    return result