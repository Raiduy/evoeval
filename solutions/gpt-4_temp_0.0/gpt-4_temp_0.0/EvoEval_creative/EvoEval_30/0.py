from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    (rows, cols) = (len(maze), len(maze[0]))
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [start])])
    while queue:
        ((x, y), path) = queue.popleft()
        if (x, y) == end:
            return path
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols and (not visited[nx][ny]) and (maze[nx][ny] == 1):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[nx][ny] = True
    return []