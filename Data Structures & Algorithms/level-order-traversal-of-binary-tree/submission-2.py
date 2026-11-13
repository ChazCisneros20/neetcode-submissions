# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [] 
        
        from collections import deque
        queue = deque() 
        queue.append(root) 
        res = [] 

        #batch dequeue 
        while len(queue) > 0 :
            breadth_layer = [] 
            for i in range(len(queue)):
                node = queue.popleft()
                breadth_layer.append(node.val) 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(breadth_layer)
        return res
                

                
        