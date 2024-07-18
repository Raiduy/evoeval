def magical_seven(n: int):
    count = 0
    num = 0
    while count < n:
        num += 1
        if num % 7 == 0:
            digits_sum = sum((int(digit) for digit in str(num)))
            if digits_sum == 7:
                count += 1
    return num