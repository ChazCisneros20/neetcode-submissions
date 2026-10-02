# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        res = []
        #// batch BFS queueing
        queue.append(root)
        while len(queue) > 0:
            temp_batch=[]
            for i in range(len(queue)):
                root = queue.popleft()
                temp_batch.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(temp_batch)
        return res 

                
        