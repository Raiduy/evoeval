
def mixed_solution(arr):
    sum_odd = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            digits_sum = sum((int(digit) for digit in str(abs(arr[i]))))
            if digits_sum > 0:
                sum_odd += arr[i]
    return sum_odd