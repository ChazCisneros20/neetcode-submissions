class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0 
            else:
                return -1 
        
        def binarySearch(start, end):
            if end <= start:
                if nums[start] == target:
                    return start
                else:
                    return -1 
            mid=(start+end)//2
            if nums[start] <= nums[mid] <= nums[end]:
                if target < nums[mid]:
                    return binarySearch(start, mid)
                elif target>nums[mid]:
                    return binarySearch(mid+1, end)
                else: #// found
                    return mid 
            elif nums[start] <= nums[mid]: #// if left-half sorted
                if nums[start] <= target <= nums[mid]: #// if left-half sorted AND target is between the values
                    return binarySearch(start, mid)
                else: #// if left-half sorted and target NOT between those values 
                    return binarySearch(mid+1, end)
            else: #// if right-half is sorted
                if nums[mid] < target <= nums[end]: #// if right-half sorted AND target is between those values
                    return binarySearch(mid+1, end)
                else: #// if right-half sorted and target NOT between those values 
                    return binarySearch(start, mid)

        return binarySearch(start=0, end=len(nums)-1)

