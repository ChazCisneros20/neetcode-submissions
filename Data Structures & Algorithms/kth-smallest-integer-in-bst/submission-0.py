# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def kSmallest(root, arr):
            if not root:
                return arr
            kSmallest(root.left, arr)
            arr.append(root.val)
            kSmallest(root.right, arr)
            return arr
        return kSmallest(root, arr)[k-1]
        
            
            
            

        


