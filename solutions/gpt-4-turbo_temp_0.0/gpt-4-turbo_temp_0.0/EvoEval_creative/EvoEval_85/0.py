def princess_rescue(coord, grid):
    (rows, cols) = (len(grid), len(grid[0]))
    (target_row, target_col) = coord
    if grid[0][0] == 1 or grid[target_row][target_col] == 1:
        return -1
    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    while queue:
        (row, col, moves) = queue.popleft()
        if (row, col) == (target_row, target_col):
            return moves
        for (dr, dc) in directions:
            (next_row, next_col) = (row + dr, col + dc)
            if 0 <= next_row < rows and 0 <= next_col < cols and (grid[next_row][next_col] == 0) and ((next_row, next_col) not in visited):
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, moves + 1))
    return -1