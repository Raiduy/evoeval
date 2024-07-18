
def mixed_solution(arr):
    sum = 0
    for i in range(0, len(arr), 2):
        if arr[i] % 2 != 0:
            digits_sum = sum((int(digit) for digit in str(abs(arr[i]))))
            if digits_sum > 0:
                sum += arr[i]
    return sum