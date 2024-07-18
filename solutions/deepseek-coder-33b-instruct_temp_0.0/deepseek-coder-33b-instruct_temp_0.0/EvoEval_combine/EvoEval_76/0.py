def sort_prime_digit_sum(lst):
    new_lst = []
    for num in lst:
        if is_prime(num):
            new_lst.append(sum_of_digits(num))
        else:
            new_lst.append(num)
    if (new_lst[0] + new_lst[-1]) % 2 == 0:
        return sorted(new_lst, reverse=True)
    else:
        return sorted(new_lst)