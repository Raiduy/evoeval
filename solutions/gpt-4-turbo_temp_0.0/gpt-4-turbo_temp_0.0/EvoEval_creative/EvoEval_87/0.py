def word_spiral(arr):
    if not arr or not arr[0]:
        return ''
    result = []
    (top, bottom) = (0, len(arr))
    (left, right) = (0, len(arr[0]))
    while top < bottom and left < right:
        for i in range(left, right):
            result.append(arr[top][i])
        top += 1
        for i in range(top, bottom):
            result.append(arr[i][right - 1])
        right -= 1
        if not (top < bottom and left < right):
            break
        for i in range(right - 1, left - 1, -1):
            result.append(arr[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            result.append(arr[i][left])
        left += 1
    return ''.join(result)