class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removals = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                removals+=1

                if i == n-1:
                    nums[i] = '_'
                else:
                    j = i
                    while j < n-1:
                        nums[j] = nums[j+1]
                        j+=1
                    nums[n-removals] = '_'
        
        K = n - removals
        return K 
                        

            