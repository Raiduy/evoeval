from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]):
    (rows, cols) = (len(maze), len(maze[0]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        ((x, y), path) = queue.popleft()
        if (x, y) == end:
            return path
        for (dx, dy) in directions:
            (new_x, new_y) = (x + dx, y + dy)
            if 0 <= new_x < rows and 0 <= new_y < cols and (maze[new_x][new_y] == 1) and ((new_x, new_y) not in visited):
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                visited.add((new_x, new_y))
    return []