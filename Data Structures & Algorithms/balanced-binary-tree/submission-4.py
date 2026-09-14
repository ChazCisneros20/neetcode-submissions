# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        def isbalanced(root, depth):
            if not root:
                return depth
            left_depth = isbalanced(root.left, depth+1)
            right_depth = isbalanced(root.right, depth+1)
            if not left_depth or not right_depth:
                return False 
            else:
                if abs(left_depth-right_depth) == 0 or abs(left_depth-right_depth) == 1:
                    return max(left_depth, right_depth)
                else:
                    return False 
        if isbalanced(root, 0):
            return True
        else:
            return False
