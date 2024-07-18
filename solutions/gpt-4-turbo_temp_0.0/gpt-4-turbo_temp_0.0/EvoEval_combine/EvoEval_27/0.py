
def list_prime_exchange(lst1, lst2, x, y):
    """The function to determine if it's possible to make lst1 a list of only prime numbers
    by exchanging elements with lst2."""
    combined_primes = [num for num in lst1 + lst2 if is_prime(num)]
    prime_count_in_lst1 = sum((is_prime(num) for num in lst1))
    non_prime_count_in_lst1 = len(lst1) - prime_count_in_lst1
    if len(combined_primes) >= len(lst1):
        return x
    else:
        return y