
def eat(number, need, remaining):
    total_eaten = number + min(need, remaining)
    remaining_carrots = remaining - min(need, remaining)
    return [total_eaten, remaining_carrots]