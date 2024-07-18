
def minPath(grid, k):
    n = len(grid)
    heap = [(grid[0][0], 0, 0, [grid[0][0]])]
    visited = set([(0, 0)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while heap:
        (val, x, y, path) = heapq.heappop(heap)
        if len(path) == k:
            return path
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n and ((nx, ny) not in visited):
                visited.add((nx, ny))
                new_path = path + [grid[nx][ny]]
                heapq.heappush(heap, (grid[nx][ny], nx, ny, new_path))
    return []