def find_pattern(mat):
    """Given a 2D matrix of integers, return a list of all elements that form an "X" pattern. 
    The "X" pattern starts from the top left corner (0, 0) and ends at the bottom right corner (n, n), 
    and starts from the top right corner (0, n) and ends at the bottom left corner (n, 0).

    Note: The matrix is square and the dimension is an odd number.

    Examples
    find_pattern([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) ==> [1, 5, 9, 3, 5, 7]
    find_pattern([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33, 34, 35]]) ==>
    [11, 17, 23, 29, 35, 15, 19, 23, 27, 31]
    find_pattern([[10, 20, 30, 40, 50, 60, 70], [80, 90, 100, 110, 120, 130, 140], [150, 160, 170, 180, 190, 200, 210], [220, 230, 240, 250, 260, 270, 280], 
    [290, 300, 310, 320, 330, 340, 350], [360, 370, 380, 390, 400, 410, 420], [430, 440, 450, 460, 470, 480, 490]]) ==>
    [10, 90, 170, 250, 330, 410, 490, 70, 130, 190, 250, 310, 370, 430]
    """
    n = len(mat)
    pattern = []
    for i in range(n):
        pattern.append(mat[i][i])
    for i in range(n):
        pattern.append(mat[i][n - i - 1])
    return pattern