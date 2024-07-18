
def minPath(grid, k):
    N = len(grid)  # Assuming the grid is square
    # Create a mapping from value to its coordinates for quick access
    value_to_pos = {}
    for i in range(N):
        for j in range(N):
            value_to_pos[grid[i][j]] = (i, j)
    
    # Helper function to get neighbors
    def get_neighbors(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < N and 0 <= y + dy < N:
                yield x + dx, y + dy
    
    # DFS function to explore all possible paths of length k
    def dfs(x, y, k, path, visited, best):
        if k == 0:
            # If a better path is found, update the best path
            if not best[0] or path < best[0]:
                best[0] = path[:]
            return
        
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                path.append(grid[nx][ny])
                dfs(nx, ny, k-1, path, visited, best)
                path.pop()
                visited.remove((nx, ny))
    
    best = [None]
    for value in range(1, N*N + 1):
        x, y = value_to_pos[value]
        dfs(x, y, k-1, [value], {(x, y)}, best)
        # Early stopping if the first cell is part of the best path
        if best[0] and best[0][0] == value:
            break
    
    return best[0]
