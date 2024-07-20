def get_magic_indices(lst):
    magic_indices = []
    for i in range(len(lst)):
        val = abs(lst[i])
        if i == 0 and val == 0:
            magic_indices.append(i)
        elif i != 0 and val % i == 0:
            product = 1
            for digit in str(val):
                product *= int(digit)
            if product == i:
                magic_indices.append(i)
    return sorted(magic_indices)