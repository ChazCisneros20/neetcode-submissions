class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, start, end, target):
            if (end-start+1)<=1: #// one element exists
                return start if nums[start]==target else -1 
            mid = (start+end)//2
            if target < nums[mid]:
                return binarySearch(nums, start, mid, target)
            elif target > nums[mid]:
                return binarySearch(nums, mid+1, end, target)
            else:
                return mid 

        return binarySearch(nums, 0, len(nums)-1, target)
            