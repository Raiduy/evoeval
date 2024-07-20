
def eat(number, need, remaining):
    eat_carrots = min(need, remaining)
    total_eaten = number + eat_carrots
    remaining_carrots = max(0, remaining - eat_carrots)
    return [total_eaten, remaining_carrots]