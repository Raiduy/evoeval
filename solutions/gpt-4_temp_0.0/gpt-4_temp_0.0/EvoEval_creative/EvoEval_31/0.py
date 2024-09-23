def unique_paths(m: int, n: int) -> int:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there from start to finish?
    >>> unique_paths(3, 2)
    3
    >>> unique_paths(7, 3)
    28
    >>> unique_paths(3, 3)
    6

    :param m: the number of rows in the grid
    :param n: the number of columns in the grid
    :return: the number of possible unique paths from start to finish
    """
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]