

def pairs_sum_to_zero(l):
    seen_numbers = set()
    for number in l:
        if -number in seen_numbers:
            return True
        seen_numbers.add(number)
    return False