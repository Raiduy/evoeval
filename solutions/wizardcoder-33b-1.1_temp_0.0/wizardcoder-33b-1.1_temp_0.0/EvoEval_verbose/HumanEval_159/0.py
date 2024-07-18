
def eat(number, need, remaining):
    if not all((isinstance(i, int) and 0 <= i <= 1000 for i in [number, need, remaining])):
        raise ValueError('All inputs must be non-negative integers not exceeding 1000.')
    total_eaten = number + min(need, remaining)
    remaining_carrots = max(remaining - need, 0)
    return [total_eaten, remaining_carrots]