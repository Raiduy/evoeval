def sort_prime_digit_sum(lst):
    """
    You are given a list of non-negative integers. First, for each integer, if it is a prime number, 
    replace it with the sum of its digits; if not, keep it as is. Then, return a copy of the modified list 
    after sorting, where you will sort the list in ascending order if the sum of the first and last index value 
    is odd, or sort it in descending order if the sum of the first and last index value is even.

    Note:
    * don't change the original list.

    Examples:
    * sort_prime_digit_sum([]) => []
    * sort_prime_digit_sum([5]) => [5]
    * sort_prime_digit_sum([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_prime_digit_sum([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    * sort_prime_digit_sum([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) => [0, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 7, 10, 32, 32, 32, 324]
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n):
        return sum((int(digit) for digit in str(n)))
    modified_lst = [digit_sum(num) if is_prime(num) else num for num in lst]
    if (modified_lst[0] + modified_lst[-1]) % 2 == 0:
        return sorted(modified_lst, reverse=True)
    else:
        return sorted(modified_lst)