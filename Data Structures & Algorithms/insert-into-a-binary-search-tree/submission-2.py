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
        #// Perform binary search
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        #// this will never FIND the value, as we are inserting
        #// a non-duplicate value in this data structure.
        #// so in the case we "almost" find it, it will be the lowest NULL/None
        #// value, which should turn into a TreeNode with `val` and stick to that
        #// .left or .right link
        return root 