def magical_sequence(start, end, divisor):
    result = []
    for i in range(start, end + 1):
        if i % divisor == 0 and is_prime(i):
            result.append(i)
    return result