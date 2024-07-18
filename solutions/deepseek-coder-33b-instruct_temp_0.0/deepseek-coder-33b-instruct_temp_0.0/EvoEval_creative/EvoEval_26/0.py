def pathfinder(maze, start, end):
    if start == end:
        return []
    directions = [(0, 1, 'right'), (0, -1, 'left'), (1, 0, 'down'), (-1, 0, 'up')]
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
            (x, y, direction_str) = direction
            (next_x, next_y) = (current[0] + x, current[1] + y)
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and (maze[next_x][next_y] == 0):
                queue.append(((next_x, next_y), path + [direction_str]))
    return []