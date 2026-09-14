# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if not root:
                return [True, 0]
            left = balanced(root.left)
            right = balanced(root.right)
            left_depth = 1 + left[1]
            right_depth = 1 + right[1]

            #// if prior subtrees came back balanced
            if (left[0] and right[0]) and ( abs(left_depth-right_depth) <= 1 ):
                return [True, max(left_depth, right_depth)]
            else:
                return [False, max(left_depth, right_depth)]
        return balanced(root)[0]
        
        

