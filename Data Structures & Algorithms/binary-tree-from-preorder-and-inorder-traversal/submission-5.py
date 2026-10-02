# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {inorder[i] : i for i in range(len(inorder))}
        #global preorder index that increments every root created
        self.preorder_index = 0
        def build(l, r): #// rather than slicing subarrays on left and right sides with a mid
            if l > r: #// if < 1 element, should become a [None]
                return None 
            first_value = preorder[self.preorder_index]
            self.preorder_index+=1
            mid_index = inorderMap[first_value]  #O(1) lookup of the preorder value's index in the inorder array
            root = TreeNode(first_value)
            root.left = build(l, mid_index-1)
            root.right = build(mid_index+1, r)
            return root 
        return build(0, len(inorder)-1) 