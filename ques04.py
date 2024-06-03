def max_border(n, m, grid):
    def dfs(x, y, shape_id):
        stack = [(x, y)]
        shape = []
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            shape.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 'B':
                    stack.append((nx, ny))
        return shape
    
    visited = [[False] * m for _ in range(n)]
    shapes = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B' and not visited[i][j]:
                shapes.append(dfs(i, j, len(shapes)))
    
    max_border = 0
    
    for shape in shapes:
        rows = {}
        cols = {}
        for x, y in shape:
            if x not in rows:
                rows[x] = 0
            if y not in cols:
                cols[y] = 0
            rows[x] += 1
            cols[y] += 1
        max_border = max(max_border, max(rows.values()), max(cols.values()))
    
    return max_border

# Example usage:
n = 4
m = 5
grid = [
    ['W', 'B', 'B', 'W', 'W'],
    ['W', 'B', 'B', 'W', 'B'],
    ['W', 'W', 'W', 'B', 'B'],
    ['B', 'B', 'W', 'W', 'W']
]

print("Maximum Border:", max_border(n, m, grid))
