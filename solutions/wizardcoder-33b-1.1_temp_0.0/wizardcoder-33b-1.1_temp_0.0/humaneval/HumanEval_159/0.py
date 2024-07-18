
def eat(number, need, remaining):
    total_eaten = number + need
    remaining_carrots = remaining - need
    if remaining_carrots < 0:
        remaining_carrots = 0
    return [total_eaten, remaining_carrots]
