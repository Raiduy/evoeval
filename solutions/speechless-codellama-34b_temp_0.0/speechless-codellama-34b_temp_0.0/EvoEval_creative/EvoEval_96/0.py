def get_magic_indices(lst):
    magic_indices = []
    for i in range(len(lst)):
        if lst[i] % i == 0 and prod_digits(lst[i]) == i:
            magic_indices.append(i)
    return magic_indices