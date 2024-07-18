def pathfinder(maze, start, end):
    if start == end:
        return []
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    direction_names = ['right', 'left', 'down', 'up']

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or (col >= cols) or (maze[row][col] == 1) or visited[row][col]:
            return False
        visited[row][col] = True
        if (row, col) == end:
            return True
        for i in range(len(directions)):
            new_row = row + directions[i][0]
            new_col = col + directions[i][1]
            if dfs(new_row, new_col):
                return True
        return False
    if dfs(start[0], start[1]):
        path = []
        (row, col) = start
        while (row, col) != end:
            for i in range(len(directions)):
                new_row = row + directions[i][0]
                new_col = col + directions[i][1]
                if new_row >= 0 and new_row < rows and (new_col >= 0) and (new_col < cols) and visited[new_row][new_col]:
                    path.append(direction_names[i])
                    row = new_row
                    col = new_col
                    break
        return path
    return []