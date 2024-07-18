def spider_web_jump(arr):
    (n, m) = (len(arr), len(arr[0]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    min_energy = [[float('inf')] * m for _ in range(n)]
    min_energy[0][0] = arr[0][0]
    heap = [(arr[0][0], 0, 0)]
    while heap:
        (energy, x, y) = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if arr[x][y] == 0:
            return energy
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < m and (not visited[nx][ny]):
                new_energy = energy + arr[nx][ny]
                if new_energy < min_energy[nx][ny]:
                    min_energy[nx][ny] = new_energy
                    heapq.heappush(heap, (new_energy, nx, ny))
    return -1