# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [] 
        def kSmallest(root, k, res):
            if not root:
                return res
            #// in-order traverse 
            kSmallest(root.left, k, res)
            res.append(root.val)
            kSmallest(root.right, k, res)
            return res
        return kSmallest(root,k, res)[k-1]