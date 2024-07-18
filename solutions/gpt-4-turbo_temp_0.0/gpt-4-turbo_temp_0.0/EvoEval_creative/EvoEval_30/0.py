from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]) -> List[Tuple[int, int]]:
    (rows, cols) = (len(maze), len(maze[0]))
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])
    while queue:
        ((current, path), queue) = (queue[0], queue[1:])
        (r, c) = current
        if current == end:
            return path
        visited[r][c] = True
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (rr, cc) = (r + dr, c + dc)
            if 0 <= rr < rows and 0 <= cc < cols and (not visited[rr][cc]) and (maze[rr][cc] == 1):
                queue.append(((rr, cc), path + [(rr, cc)]))
    return []