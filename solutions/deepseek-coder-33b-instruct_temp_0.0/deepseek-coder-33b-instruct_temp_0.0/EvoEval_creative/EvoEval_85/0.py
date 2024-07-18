def princess_rescue(coord, grid):
    (rows, cols) = (len(grid), len(grid[0]))
    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    while queue:
        (row, col, steps) = queue.popleft()
        if (row, col) == coord:
            return steps
        for (dr, dc) in directions:
            (nr, nc) = (row + dr, col + dc)
            if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 0) and ((nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return -1