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
        def inorder(root, res):
            if not root:
                return res
            if not root.left:
                res.append(root.val)
                inorder(root.right, res)
                return res
            #// get the leftmost depthmost value
            inorder(root.left, res)
            #// go up by one to the parent, append that value
            res.append(root.val)
            #// perform same above operations on now the RIGHT SUBTREE
            inorder(root.right, res)
            return res
        return inorder(root, res)
        