def pathfinder(maze, start, end):
    directions = [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]
    visited = set()
    path = []
    successful_path = []

    def dfs(position):
        if position == end:
            successful_path.extend(path)
            return True
        visited.add(position)
        for (d_row, d_col, direction) in directions:
            new_position = (position[0] + d_row, position[1] + d_col)
            if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]) and (maze[new_position[0]][new_position[1]] == 0):
                if new_position not in visited:
                    path.append(direction)
                    if dfs(new_position):
                        return True
                    path.pop()
        visited.remove(position)
        return False
    dfs(start)
    return successful_path