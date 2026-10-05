# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def pathSum(root, current_sum):
            if not root:
                return False 
            current_sum+=root.val
            if not root.left and not root.right: # we hit a leaf
                return True if current_sum == targetSum else False
            if pathSum(root.left, current_sum):
                return True
            if pathSum(root.right, current_sum):
                return True
            return False 
        return pathSum(root, 0)
