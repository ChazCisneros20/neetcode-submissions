class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        #Make array of 2n length, initialize with default values 
        ans = [0]*(2*n)
        for i in range(0, n):
            ans[i] = nums[i]
            ans[n+i] = nums[i]
        return ans