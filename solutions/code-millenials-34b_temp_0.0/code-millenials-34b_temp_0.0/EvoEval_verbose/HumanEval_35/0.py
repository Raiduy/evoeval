

def max_element(l: list):
    max_val = l[0]
    for num in l:
        if num > max_val:
            max_val = num
    return max_val