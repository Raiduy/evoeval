def sort_prime_digit_sum(lst):
    new_lst = lst[:]
    for i in range(len(new_lst)):
        if is_prime(new_lst[i]):
            new_lst[i] = digit_sum(new_lst[i])
    if (new_lst[0] + new_lst[-1]) % 2 == 0:
        return sorted(new_lst, reverse=True)
    else:
        return sorted(new_lst)