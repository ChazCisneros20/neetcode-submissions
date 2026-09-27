# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None 
        def minNodeSearch(root):
            curr = root 
            while curr and curr.left:
                curr = curr.left 
            return curr

        def deleteBinarySearch(root, key):
            if not root:
                return None
            if key < root.val:
                root.left = deleteBinarySearch(root.left, key)
            elif key > root.val:
                root.right = deleteBinarySearch(root.right, key)
            else: #// key==root.val
                #// check 0/1 children or 2 children
                if not root.left:
                    return root.right  #// b/c past call is root.right=/root.left= so this will 
                    #// make the delete node just BE the single child. and the pointers will be lost
                    #// "deleting" the root 
                if not root.right:
                    return root.left 
                #// if not root.right and not root.left:
                minNode = minNodeSearch(root.right)
                root.val = minNode.val 
                root.right = deleteBinarySearch(root.right, minNode.val)
            return root 
        return deleteBinarySearch(root, key)
