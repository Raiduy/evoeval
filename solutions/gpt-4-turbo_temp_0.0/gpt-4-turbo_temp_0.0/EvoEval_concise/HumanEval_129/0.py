
def minPath(grid: List[List[int]], k: int) -> List[int]:
    if not grid or k <= 0:
        return []
    N = len(grid)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    min_path = [float('inf')]

    def dfs(x, y, path, steps):
        nonlocal min_path
        if steps == k:
            if path < min_path:
                min_path = path.copy()
            return
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < N and 0 <= ny < N:
                path.append(grid[nx][ny])
                dfs(nx, ny, path, steps + 1)
                path.pop()
    for i in range(N):
        for j in range(N):
            dfs(i, j, [grid[i][j]], 1)
    return min_path