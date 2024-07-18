def string_sequence_modified(n: int, m: int) -> str:
    result = []
    for i in range(n + 1):
        if i % m == 0:
            result.append('FizzBuzz' if i % m == 0 else 'Fizz')
        else:
            result.append(str(i))
    return ' '.join(result)