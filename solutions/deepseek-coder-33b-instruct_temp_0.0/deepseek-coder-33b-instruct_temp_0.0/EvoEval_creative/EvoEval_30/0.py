from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]) -> List[Tuple[int]]:
    (rows, cols) = (len(maze), len(maze[0]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set(start)
    while queue:
        (current, path) = queue.popleft()
        if current == end:
            return path
        for direction in directions:
            (next_row, next_col) = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next_row < rows and 0 <= next_col < cols and (maze[next_row][next_col] == 1) and ((next_row, next_col) not in visited):
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))
                visited.add((next_row, next_col))
    return []