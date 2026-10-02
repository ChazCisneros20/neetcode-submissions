class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def comboSum(i, temp_arr, total): #// pass total for O(1) check, dont re-sum
            if total == target:
                res.append(temp_arr.copy())
                return 
            elif total > target or i >= len(nums):
                return 
            temp_arr.append(nums[i])
            total+=nums[i]
            comboSum(i, temp_arr, total)
            temp_arr.pop()
            total-=nums[i]
            comboSum(i+1, temp_arr, total)

        comboSum(0, [], 0)
        return res
                