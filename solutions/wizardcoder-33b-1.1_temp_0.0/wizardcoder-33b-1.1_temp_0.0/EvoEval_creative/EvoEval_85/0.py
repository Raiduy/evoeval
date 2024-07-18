def princess_rescue(coord, grid):
    if grid[coord[0]][coord[1]] == 1:
        return -1
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    directions = [(0, 1), (1, 0)]
    while queue:
        (x, y, steps) = queue.popleft()
        if (x, y) == coord:
            return steps
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == 0) and ((nx, ny) not in visited):
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))
    return -1