def spider_web_jump(arr):
    (rows, cols) = (len(arr), len(arr[0]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, energy):
        if not is_valid(x, y) or arr[x][y] >= 100:
            return float('inf')
        if arr[x][y] == 0:
            return energy
        temp = arr[x][y]
        arr[x][y] = 100
        res = min([dfs(x + dx, y + dy, energy + temp) for (dx, dy) in directions if is_valid(x + dx, y + dy)])
        arr[x][y] = temp
        return res
    return dfs(0, 0, 0)