def princess_rescue(coord, grid):
    (rows, cols) = (len(grid), len(grid[0]))
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(0, 0, 0)])
    directions = [(0, 1), (1, 0)]
    while queue:
        (r, c, steps) = queue.popleft()
        if r == coord[0] and c == coord[1]:
            return steps
        for (dr, dc) in directions:
            (nr, nc) = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols and (not visited[nr][nc]) and (grid[nr][nc] == 0):
                visited[nr][nc] = True
                queue.append((nr, nc, steps + 1))
    return -1