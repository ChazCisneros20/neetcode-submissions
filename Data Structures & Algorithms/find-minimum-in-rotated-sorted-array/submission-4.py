class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(s,e,nums):
            if e==s:
                return nums[s]
            mid = (s+e)//2
            if nums[mid] < nums[e]: #// if yes, it means it SOMEWHERE in left half
                return binarySearch(s, mid, nums)
            else:#// else its in right half
                return binarySearch(mid+1, e, nums)
            
        return binarySearch(0, len(nums)-1, nums)