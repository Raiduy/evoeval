def get_magic_indices(lst):
    magic_indices = []
    for i in range(len(lst)):
        val = lst[i]
        if val == 0:
            if i == 0:
                magic_indices.append(i)
        elif val > 0 and val % i == 0:
            if val == 1 or val == -1:
                if i == 0:
                    magic_indices.append(i)
            else:
                product = 1
                while val > 0:
                    digit = val % 10
                    product *= digit
                    val //= 10
                if product == i:
                    magic_indices.append(i)
    return magic_indices