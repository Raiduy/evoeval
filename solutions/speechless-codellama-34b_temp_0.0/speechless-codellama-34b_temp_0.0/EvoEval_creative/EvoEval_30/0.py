from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]) -> List[Tuple[int]]:

    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (maze[x][y] == 1)

    def bfs():
        queue = [(start, [start])]
        visited = set([start])
        while queue:
            ((x, y), path) = queue.pop(0)
            if (x, y) == end:
                return path
            for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                (nx, ny) = (x + dx, y + dy)
                if is_valid(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return []
    return bfs()