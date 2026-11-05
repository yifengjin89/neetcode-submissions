# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        
        q = deque([(p, q)])
        while q:
            a, b = q.popleft()
            if a.val != b.val:
                return False

            if (not a.left and b.left) or (not b.left and a.left):
                return False
            if (not a.right and b.right) or (not b.right and a.right): 
                return False

            if a.left and b.left:
                q.append((a.left, b.left))
            
            if a.right and b.right:
                q.append((a.right, b.right))

        return True
            
        