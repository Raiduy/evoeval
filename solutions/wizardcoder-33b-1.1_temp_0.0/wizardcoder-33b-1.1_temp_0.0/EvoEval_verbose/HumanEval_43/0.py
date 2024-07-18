

def pairs_sum_to_zero(l):
    elements = set(l)
    for element in l:
        if -element in elements:
            if -element != element:
                return True
    return False