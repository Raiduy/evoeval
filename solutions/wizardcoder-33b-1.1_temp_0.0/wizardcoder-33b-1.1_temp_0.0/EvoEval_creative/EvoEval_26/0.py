def pathfinder(maze, start, end):
    if start == end:
        return []
    directions = [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]
    queue = deque([(start, [])])
    visited = set()
    while queue:
        (current, path) = queue.popleft()
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction in directions:
            (next_row, next_col) = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next_row < len(maze) and 0 <= next_col < len(maze[0]) and (maze[next_row][next_col] == 0):
                queue.append(((next_row, next_col), path + [direction[2]]))
    return []