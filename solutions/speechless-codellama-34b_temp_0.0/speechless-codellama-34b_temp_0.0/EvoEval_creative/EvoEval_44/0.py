def fairy_tale_transport(q, w, e):
    total_weight = sum(q)
    unicorn_capacity = w
    dragon_griffin_capacity = e
    if total_weight <= unicorn_capacity + dragon_griffin_capacity:
        return True
    else:
        return False