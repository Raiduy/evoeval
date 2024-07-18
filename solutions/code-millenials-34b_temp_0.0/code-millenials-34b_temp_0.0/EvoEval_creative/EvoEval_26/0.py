def pathfinder(maze, start, end):
    if start == end:
        return []
    num_rows = len(maze)
    num_cols = len(maze[0])
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    queue = [(start, [])]
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    while queue:
        (current, path) = queue.pop(0)
        if current == end:
            return path
        visited[current[0]][current[1]] = True
        for (direction, (dy, dx)) in directions.items():
            (new_x, new_y) = (current[0] + dy, current[1] + dx)
            if 0 <= new_x < num_rows and 0 <= new_y < num_cols and (not visited[new_x][new_y]) and (maze[new_x][new_y] == 0):
                queue.append(((new_x, new_y), path + [direction]))
    return []