# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #// we need to do BFS traversal but only append to res[] array the rightmost nodes of the BFS breadth level. 
        res = []
        if not root:
            return res 
        queue = deque()
        queue.append(root)
        #// this is where batch-based BFS traversal is key. 
        while len(queue) > 0:
            #// b/c we want the rightmost node of each breadth bfs layer, 
            #// we are asking for the n-1 node. 
            breadth_n = len(queue)
            for i in range(breadth_n):
                node = queue.popleft()
                if i == breadth_n - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res

            