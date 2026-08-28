class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        s = 0
        e = n-1
        
        while s <= e:
            #Distance version, but generally it is m = (e+s)//2
            m = s + (e-s) // 2
            if nums[m] == target:
                return m 
            elif target < nums[m]:
                e = m-1
            else:#// target > nums[m]:
                s = m+1
        #// if it never reaches `nums[m] == target`
        return -1 

        