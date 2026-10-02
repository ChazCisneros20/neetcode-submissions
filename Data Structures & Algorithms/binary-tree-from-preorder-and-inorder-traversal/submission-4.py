# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {inorder[i] : i for i in range(len(inorder))}
        self.pre_index = 0
        def build(l, r):
            if l > r:
                return None 
            first_value = preorder[self.pre_index]
            self.pre_index+=1 
            mid = inorderMap[first_value] #mid == inorder_index (our pointer)
            
            root = TreeNode(first_value)
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root 


        return build(0, len(preorder)-1)
