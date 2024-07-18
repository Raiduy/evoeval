def spider_web_jump(arr):
    (rows, cols) = (len(arr), len(arr[0]))
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    while queue:
        (row, col, energy) = queue.popleft()
        if arr[row][col] == 0:
            return energy
        for (dr, dc) in directions:
            (new_row, new_col) = (row + dr, col + dc)
            if 0 <= new_row < rows and 0 <= new_col < cols and ((new_row, new_col) not in visited):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, energy + arr[row][col]))
    return -1