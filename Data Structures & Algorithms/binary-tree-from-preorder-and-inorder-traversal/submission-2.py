# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderIndicesHashmap = { inorder[i]:i for i in range(len(inorder))}
        self.preorder_index = 0
        def DFS(l, r): 
            #// use the classic merge/quicksort method of making sure things dont go out of bounds
            #// but make sure that [l] and [r] are ALLOWED TO BE EQUIVALENT. 
            #// BECAUSE a node can exist as a new root and child of a parent, 
            #// but also contain no child nodes of their own. if dfs(4,4) uses [2] from `inorder` then
            #// we need to account for that being allowed. it just means [2] will not get a .left or .right
            #// child/subtree
            if l > r:
                return None
            #// Init your node ===
            root_value = preorder[self.preorder_index]
            self.preorder_index+=1
            root = TreeNode(root_value)
            #// re-anchor the current [mid] pointer for [inorder] array
            #// using the precomputed hashmap for O(1) [inorder] array index lookup {inorder_value : inorder_index}
            mid = inorderIndicesHashmap[root_value]
            #// Create left and right subtrees of root based on 
            #// the inorder indices 
            root.left = DFS(l, mid-1)
            root.right= DFS(mid+1, r)
            return root 
        
        return DFS(0, len(inorder)-1)