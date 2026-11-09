"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hashmap = {node: Node(node.val)}
        q = deque([node])
        while q:
            old = q.popleft()
            for nei in old.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)

                hashmap[old].neighbors.append(hashmap[nei])
        
        return hashmap[node]
        