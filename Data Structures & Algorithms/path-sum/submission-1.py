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
        def HasPathSum(root, pathSum, targetSum):
            if not root:
                return False 
            pathSum+=root.val 
            if not root.left and not root.right:
                if pathSum == targetSum:
                    return True 
            if HasPathSum(root.left, pathSum, targetSum): #// if left subtree finds a suitable path, it returns True up
                return True
            if HasPathSum(root.right, pathSum, targetSum):
                return True 
            #// if the current pathSum isn't targetSum AND neither subtrees to their root->leaf found a pathSum:
            return False 
        return HasPathSum(root, 0, targetSum)
                
        