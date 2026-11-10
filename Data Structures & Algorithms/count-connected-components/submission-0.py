class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        #{0:[1],1:[0,2],2:[1], 3:[4], 4:[3]}
        visited = set()

        total = 0
        for i in range(n):
            if i not in visited:
                self.bfs(graph, visited, i)
                total += 1

        return total
    
    def bfs(self, graph, visited, i):
        q = deque([i])
        visited.add(i)

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        