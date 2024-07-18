def helper(n, steps, memo):
    """
    Helper function to calculate the number of distinct ways to reach `n` using the available `steps`.
    This function uses memoization to store and reuse previously calculated results.
    """
    if n == 0:
        return 1  # Base case: There is 1 way to reach 0 (by not taking any steps)
    if n < 0:
        return 0  # Invalid case: We cannot reach a negative value

    if n in memo:
        return memo[
            n
        ]  # Retrieve the result from the memoization dictionary if available

    ways = 0
    for step in steps:
        ways += helper(n - step, steps, memo)

    memo[n] = ways  # Store the calculated result in the memoization dictionary
    return ways
def count_ways(n, steps):
    """ 
    Given a number `n` and a list of `steps` available, calculate the number of distinct ways to reach `n` using only the steps in the list. You may use each step multiple times and you can use them in any order.

    The number `n` will be a positive integer and the list `steps` will contain positive integers. 

    For example: 
    count_ways(4, [1, 2]) == 5 
    count_ways(3, [1, 2, 3]) == 4
    count_ways(10, [2, 5]) == 2

    Note: In the first example, the ways to reach 4 using 1 and 2 are: [1,1,1,1], [2,2], [1,1,2], [1,2,1], [2,1,1].
    """
    memo = {}
    return helper(n, steps, memo)