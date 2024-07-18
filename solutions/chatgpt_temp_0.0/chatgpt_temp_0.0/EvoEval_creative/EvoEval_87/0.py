def word_spiral(arr):
    """Create a function which takes in a 2D array of characters and returns a 
    string which represents the words in the array read in a clockwise spiral starting
    from the top left corner. If the array is empty, return an empty string. 

    Examples:
    assert word_spiral([['h','i','!'],['b','y','e']]) == 'hi!eyb'
    assert word_spiral([['l','o','v','e'],['i','s','i','n'],['t','h','e','a'],['i','r', '!','!!']]) == 'lovena!!!ritisieh'
    assert word_spiral([]) == ''
    """
    if not arr:
        return ''
    result = ''
    top_row = 0
    bottom_row = len(arr) - 1
    left_col = 0
    right_col = len(arr[0]) - 1
    while top_row <= bottom_row and left_col <= right_col:
        for i in range(left_col, right_col + 1):
            result += arr[top_row][i]
        top_row += 1
        for i in range(top_row, bottom_row + 1):
            result += arr[i][right_col]
        right_col -= 1
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                result += arr[bottom_row][i]
            bottom_row -= 1
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                result += arr[i][left_col]
            left_col += 1
    return result