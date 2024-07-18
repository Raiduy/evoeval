
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(grid[0][0], 0, 0, [grid[0][0]])]
    visited = {(0, 0): grid[0][0]}
    while heap:
        (cost, x, y, path) = heapq.heappop(heap)
        if len(path) == k:
            return path
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n and ((nx, ny) not in visited):
                visited[nx, ny] = grid[nx][ny]
                heapq.heappush(heap, (cost + grid[nx][ny], nx, ny, path + [grid[nx][ny]]))
    return []