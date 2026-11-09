DIR = [(0, 1), (0, -1), (1, 0), (-1,0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not any(grid):
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        total = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited: 
                    self.bfs(grid, visited, m, n, i, j)
                    total += 1

        return total
    
    def bfs(sefl, grid, visited, m, n, i, j):
        q = deque([(i, j)])
        visited.add((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in DIR:
                nx = dx + x
                ny = dy + y
                if (0 <= nx < m and 0 <= ny < n) and (nx, ny) not in visited and grid[nx][ny] == "1":
                    q.append((nx, ny))
                    visited.add((nx, ny))