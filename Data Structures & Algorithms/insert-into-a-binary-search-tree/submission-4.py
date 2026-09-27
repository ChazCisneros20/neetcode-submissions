# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insertBST(root, val):
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = insertBST(root.left, val)
            else:
                root.right = insertBST(root.right, val)
            return root 
        return insertBST(root,val)