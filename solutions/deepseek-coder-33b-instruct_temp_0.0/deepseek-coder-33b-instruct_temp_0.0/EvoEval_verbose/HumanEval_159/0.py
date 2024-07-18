
def eat(number, need, remaining):
    if not 0 <= number <= 1000 or not 0 <= need <= 1000 or (not 0 <= remaining <= 1000):
        raise ValueError('All inputs must be non-negative integers not exceeding 1000.')
    total_eaten = number + min(need, remaining)
    remaining_carrots = max(0, remaining - need)
    return [total_eaten, remaining_carrots]