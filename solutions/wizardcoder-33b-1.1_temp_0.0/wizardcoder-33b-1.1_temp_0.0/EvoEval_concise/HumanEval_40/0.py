

def triples_sum_to_zero(l: list):
    if len(l) < 3:
        return False
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        l_i = l[i]
        start = i + 1
        end = len(l) - 1
        while start < end:
            if l_i + l[start] + l[end] == 0:
                return True
            elif l_i + l[start] + l[end] < 0:
                current_start = start
                while l[start] == l[current_start] and start < end:
                    start += 1
            else:
                end -= 1
    return False