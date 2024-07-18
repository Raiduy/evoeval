def princess_rescue(coord, grid):
    queue = [(0, 0, 0)]
    directions = [(0, 1), (1, 0)]
    (n, m) = (len(grid), len(grid[0]))
    goal = coord
    visited = [[False] * m for _ in range(n)]
    while queue:
        (x, y, moves) = queue.pop(0)
        if (x, y) == goal:
            return moves
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < m and (not visited[nx][ny]) and (grid[nx][ny] == 0):
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
    return -1