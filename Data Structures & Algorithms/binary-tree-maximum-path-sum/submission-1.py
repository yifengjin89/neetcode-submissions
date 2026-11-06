# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_val = [float('-inf')]
        self.dfs(root, max_val)
        return max_val[0]
    
    def dfs(self, root, max_val):
        if not root:
            return 0
        
        left = max(0, self.dfs(root.left, max_val))
        right = max(0, self.dfs(root.right, max_val))

        curr_val = root.val
        max_val[0] = max(max_val[0],  left + right + curr_val)
        return curr_val + max(left, right)