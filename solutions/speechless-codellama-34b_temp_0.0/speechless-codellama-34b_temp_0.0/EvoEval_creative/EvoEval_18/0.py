def magical_seven(n: int) -> int:
    num = 7
    count = 0
    while count < n:
        if sum((int(digit) for digit in str(num))) == 7:
            count += 1
        num += 7
    return num