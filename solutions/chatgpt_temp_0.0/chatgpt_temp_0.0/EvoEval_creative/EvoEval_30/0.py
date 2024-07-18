from typing import List, Tuple

def find_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]) -> List[Tuple[int]]:
    """Returns the shortest path from start to end in a maze represented by a 2D array.

    The maze is a 2D array where 0s represent walls and 1s represent open paths. The start and end points 
    are tuples representing coordinates in the 2D array. The function should return a list of points 
    representing the shortest path from start to end. If no path is possible, return an empty list.

    >>> maze = [[1,0,1,1,1], [1,0,1,0,1], [1,1,1,0,1], [1,0,0,0,1], [1,1,1,1,1]]
    >>> start = (0,0)
    >>> end = (4, 4)
    >>> find_path(maze, start, end)
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    >>> maze = [[1,0,1], [0,0,1], [1,1,1]]
    >>> start = (0,0)
    >>> end = (2, 2)
    >>> find_path(maze, start, end)
    []
    """
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []

    def dfs(row: int, col: int) -> bool:
        if row < 0 or row >= rows or col < 0 or (col >= cols) or (maze[row][col] == 0) or visited[row][col]:
            return False
        visited[row][col] = True
        path.append((row, col))
        if (row, col) == end:
            return True
        if dfs(row + 1, col) or dfs(row - 1, col) or dfs(row, col + 1) or dfs(row, col - 1):
            return True
        path.pop()
        return False
    if dfs(start[0], start[1]):
        return path
    return []