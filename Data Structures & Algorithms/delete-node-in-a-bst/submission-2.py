# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNodeValue(self, root):
        curr = root
        #// Traverse to find the leftmost node (which is == smallest node of entire subtree)
        while curr and curr.left:
            curr = curr.left
        return curr 

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        #// Binary Search for the target node/value
        if key < root.val:
            #// This should always properly point to its root.left/right node 
            #// UNLESS it's the target node/value
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:   #// <- target node is FOUND
            #// TWO CASES: 1.) target node has 0/1 children. 
            #//            2.) target node has 2 children. 
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left 
            else: 
                #// We are doing the right subtree for "In-Order Sucessor"
                #// This ASSUMES that root has an existing root.left and root.right node.
                minNode = self.minNodeValue(root.right)
                root.val = minNode.val 
                #// Now perform an entire new recursive removal process on the minNode we 
                #// took the value from. This is to stop having duplicate nodes. 
                #// How do we target it? pass minNode.val as the NEW target value [`key`]
                root.right = self.deleteNode(root.right, minNode.val)
                #// This would be .left if we did left subtree "In-Order Sucessor"
        return root 
                
            