class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        def comboSum(i, temp_array, total): #// remember, only LEAVES can be considered. 
            if i >= len(nums) or total > target:
                return 
            elif total == target:
                res.append(temp_array.copy())
                return
            #// left path: append nums[i]
            temp_array.append(nums[i]) 
            comboSum(i, temp_array, total+nums[i])
            temp_array.pop() 
            comboSum(i+1, temp_array, total)
        comboSum(0, [], 0)
        return res