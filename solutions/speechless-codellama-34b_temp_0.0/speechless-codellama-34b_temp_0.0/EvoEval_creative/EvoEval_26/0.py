def pathfinder(maze, start, end):
    directions = []
    if start == end:
        return []
    elif maze[start[0]][start[1]] == 1:
        return []
    elif start[0] < end[0]:
        directions.append('down')
        start = (start[0] + 1, start[1])
    elif start[0] > end[0]:
        directions.append('up')
        start = (start[0] - 1, start[1])
    elif start[1] < end[1]:
        directions.append('right')
        start = (start[0], start[1] + 1)
    elif start[1] > end[1]:
        directions.append('left')
        start = (start[0], start[1] - 1)
    else:
        return []
    return directions + pathfinder(maze, start, end)