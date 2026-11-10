class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, alt = deque(), deque()
        pac_visited, alt_visited = set(), set()

        m, n = len(heights), len(heights[0])

        for col in range(n):
            pac.append((0, col))
            pac_visited.add((0, col))

            alt.append((m-1, col))
            alt_visited.add((m-1, col))


        for row in range(m):
            pac.append((row, 0))
            pac_visited.add((row, 0))

            alt.append((row, n-1))
            alt_visited.add((row, n-1))
        
        self.bfs(heights, pac, pac_visited, m, n)
        self.bfs(heights, alt, alt_visited, m, n)

        return list(pac_visited & alt_visited)
    
    def bfs(self, grid, q, visited, m, n):
        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= grid[x][y] and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
    