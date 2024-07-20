def pathfinder(maze, start, end):
    if start == end:
        return []
    (rows, cols) = (len(maze), len(maze[0]))
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [])])
    directions = [(0, 1, 'right'), (0, -1, 'left'), (1, 0, 'down'), (-1, 0, 'up')]
    while queue:
        ((x, y), path) = queue.popleft()
        if (x, y) == end:
            return path
        for (dx, dy, direction) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols and (not visited[nx][ny]) and (maze[nx][ny] == 0):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [direction]))
    return []