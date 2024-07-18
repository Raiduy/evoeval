def spider_web_jump(arr):
    (n, m) = (len(arr), len(arr[0]))
    visited = [[False] * m for _ in range(n)]
    heap = [(arr[0][0], 0, 0)]
    while heap:
        (energy, x, y) = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if arr[x][y] == 0:
            return energy
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < m and (not visited[nx][ny]):
                heapq.heappush(heap, (energy + arr[nx][ny], nx, ny))
    return -1