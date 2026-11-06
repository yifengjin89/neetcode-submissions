# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        i = 0

        for val in preorder[1:]:
            node = stack[-1]

            if node.val != inorder[i]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[i]:
                    node = stack.pop()
                    i += 1

                node.right = TreeNode(val)
                stack.append(node.right)

        return root