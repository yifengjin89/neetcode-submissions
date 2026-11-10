class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # {0:[1,2,3], 1:[0,4], 2:[0], 3:[0]}

        # {0:[1], 1:[0,2,3,4], 2:[1,3], 3:[2,1], 4:[1]}
        
        q = deque([0])
        visited = {0}

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        return len(visited) == n