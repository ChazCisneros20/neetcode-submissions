class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        #make a min heap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)