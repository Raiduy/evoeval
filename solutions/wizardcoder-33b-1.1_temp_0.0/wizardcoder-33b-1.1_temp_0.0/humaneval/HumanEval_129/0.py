
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0]*n for _ in range(n)]
    pq = [(grid[0][0], [(0, 0)])]
    while pq:
        total, path = heapq.heappop(pq)
        if len(path) == k:
            return [grid[x][y] for x, y in path]
        x, y = path[-1]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                heapq.heappush(pq, (total + grid[nx][ny], path + [(nx, ny)]))
