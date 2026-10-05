class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def subset(i, temp_array):
            if i == len(nums):
                res.append(temp_array.copy())
                return
            temp_array.append(nums[i])
            #//left path is to append and incremet i+=1
            subset(i+1, temp_array)
            temp_array.pop()
            subset(i+1, temp_array)
        subset(0, [])
        return res

            
