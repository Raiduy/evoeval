def smallest_change_and_sum(arr, x, y):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    After finding the minimum changes, add the value of x and y to it.

    For example:
    smallest_change_and_sum([1, 2, 3, 5, 4, 7, 9, 6], 2, 3) == 9
    smallest_change_and_sum([1, 2, 3, 4, 3, 2, 2], 1, 2) == 4
    smallest_change_and_sum([1, 2, 3, 2, 1], 3, 2) == 5
    """

    def min_changes_to_palindrome(arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]
    min_changes = min_changes_to_palindrome(arr)
    return min_changes + x + y