
def eat(number, need, remaining):
    if remaining >= need:
        total_eaten = number + need
        carrots_left = remaining - need
    else:
        total_eaten = number + remaining
        carrots_left = 0
    return [total_eaten, carrots_left]