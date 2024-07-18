
def mixed_solution(arr):
    sum = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            if sum_of_digits(arr[i]) > 0:
                sum += arr[i]
    return sum