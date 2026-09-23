class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        curr=[]
        #// treat res, current_stack, and target as global-ish variables
        #// another index based DFS algo problem similar to the `Subsets` powerset problem 
        def dfs(i, current_stack, total):
            if total == target:
                #// we found a combination!
                res.append(current_stack.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            #// append the i'th value 
            current_stack.append(nums[i])
            #// keep appending i'th value
            dfs(i, current_stack, total+nums[i]) #<- add our curr value to the total
            #// remove the value we push()'d, and try again but
            current_stack.pop()  
            #// try the i+1'th value (limits our options) [1*4*4*4...] -> [1*3*3...]
            dfs(i+1, current_stack, total) 
            
        dfs(i=0, current_stack=curr, total=0)
        return res