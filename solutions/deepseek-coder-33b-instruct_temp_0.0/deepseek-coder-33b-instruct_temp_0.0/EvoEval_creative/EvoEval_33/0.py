def magical_staircase(n: int, magic_stones: list):
    """
    Imagine a magical staircase with 'n' steps, and a collection of magic stones. Each magic stone has a unique power
    that allows the user to jump a certain number of steps in a single bound.
    For example, if there's a magic stone that has a power of 2, you can jump 2 steps at once instead of 1 step.

    Provided with the number of steps 'n' and a list of the powers of magic stones available, 
    return the number of distinct ways you can reach the top of the staircase. Assume you start from the bottom of the staircase.

    The magic_stones list contains positive integers, and n is a positive integer.

    Example:
    >>> magical_staircase(4, [1, 2])
    5
    Explanation: There are 5 distinct ways to reach the top of the staircase:
    - Jump 1 step, jump 1 step, jump 1 step, jump 1 step
    - Jump 1 step, jump 1 step, jump 2 steps
    - Jump 1 step, jump 2 steps, jump 1 step
    - Jump 2 steps, jump 1 step, jump 1 step
    - Jump 2 steps, jump 2 steps

    >>> magical_staircase(10, [1, 2, 5])
    128
    Explanation: There are 128 distinct ways to reach the top of the staircase.
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for stone in magic_stones:
            if i - stone >= 0:
                dp[i] += dp[i - stone]
    return dp[n]