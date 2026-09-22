class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset_stack = [] 
        res = [] 
        #// This problem is DFS, so we will descend leftmost recursively
        def dfs(i):
            #// keep recursively sending i, but stop when it reaches n-1
            if i >= len(nums):
                res.append(subset_stack.copy())
                return 
            subset_stack.append(nums[i]) #// [1,2,3]
            dfs(i+1)
            subset_stack.pop()
            #// send in the last subset but with the end popped
            dfs(i+1)                     #// [1,2]
            return res 
        return dfs(i=0)
