class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        res = heapq.nlargest(k, nums)
        return res[k-1]