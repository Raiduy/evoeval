def fairy_tale_transport(q, w, e):
    unicorn_capacity = w
    dragon_griffin_capacity = e
    total_capacity = unicorn_capacity + dragon_griffin_capacity
    total_weight = sum(q)
    if total_weight <= total_capacity:
        return True
    else:
        return False