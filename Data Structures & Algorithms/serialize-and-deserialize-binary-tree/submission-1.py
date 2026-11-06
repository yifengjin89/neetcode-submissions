# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node == "null":
                    level.append("null")
                else:
                    level.append(str(node.val))
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append("null")
                    
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append("null")
                  
                    
            s = "*".join(level)
            res.append(s)
        
        return "#".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 1#2*3#null*null*4*5#null*null*null*null

        if not data:
            return None
        
        levels = data.split("#")
        # ["1", "2*3", "null*null*4*5", "null*null*null*null"]
        nodes = []
        for level in levels:
            nodes.extend(level.split("*"))
        # # [
        #     ["1"],
        #     ["2", "3"],
        #     ["null", "null", "4", "5"],
        #     ["null", "null", "null", "null"]
        # ]

        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root




