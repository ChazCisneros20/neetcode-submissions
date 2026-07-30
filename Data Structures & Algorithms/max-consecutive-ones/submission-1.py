class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count+=1
            else: 
                if count > max_count:
                    max_count = count
                count = 0 
                #if max_count > count:
                #Reset count, leave max_count as highest. 
                
        if count > max_count:
            max_count = count
        return max_count

        