

def max_element(l: list):
    max_val = l[0]
    for i in range(1, len(l)):
        if l[i] > max_val:
            max_val = l[i]
    return max_val