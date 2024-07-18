from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]):
    (rows, cols) = (len(maze), len(maze[0]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set(start)
    while queue:
        (point, path) = queue.popleft()
        if point == end:
            return path
        for direction in directions:
            new_point = (point[0] + direction[0], point[1] + direction[1])
            if 0 <= new_point[0] < rows and 0 <= new_point[1] < cols and (maze[new_point[0]][new_point[1]] == 1) and (new_point not in visited):
                queue.append((new_point, path + [new_point]))
                visited.add(new_point)
    return []