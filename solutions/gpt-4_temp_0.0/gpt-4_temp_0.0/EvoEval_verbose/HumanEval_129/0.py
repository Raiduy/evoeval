
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = [(grid[0][0], 0, 0, [grid[0][0]])]
    while pq:
        (val, x, y, path) = heapq.heappop(pq)
        if len(path) == k:
            return path
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n:
                heapq.heappush(pq, (max(val, grid[nx][ny]), nx, ny, path + [grid[nx][ny]]))