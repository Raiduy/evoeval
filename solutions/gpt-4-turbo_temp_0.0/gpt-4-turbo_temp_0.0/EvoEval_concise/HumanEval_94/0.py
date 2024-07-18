

def skjkasdkd(lst):
    """Given a list of integers, this function finds the largest prime number in the list and returns the sum of its digits."""
    largest_prime = -1
    for number in lst:
        if is_prime(number) and number > largest_prime:
            largest_prime = number
    if largest_prime == -1:
        return 0
    return sum_of_digits(largest_prime)