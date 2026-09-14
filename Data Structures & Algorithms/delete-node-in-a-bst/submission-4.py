# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNodeValue(self, root):
        curr = root 
        while curr and curr.left:
            curr = curr.left 
        return curr 
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #// VALUE IS FOUND... but is it case1:0/1 children, or case2:2 children
            #//case1:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: #// case 2: runs on assumption that there IS 2 children nodes. 
                minNode = self.minNodeValue(root.right)
                root.val = minNode.val
                #// delete the min() node now using its given value. 
                root.right = self.deleteNode(root.right, minNode.val)
                
        return root