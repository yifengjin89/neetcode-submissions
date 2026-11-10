class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for next_ in graph[course]:
                indegree[next_] -= 1
                if indegree[next_] == 0:
                    q.append(next_)
        
        return taken == numCourses    


        