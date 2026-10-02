# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        res = [] 
        def DFS(root):
            if not root:
                return 
            #// keep going left.
            DFS(root.left)
            res.append(root.val)
            DFS(root.right)
        DFS(root)
        return res
