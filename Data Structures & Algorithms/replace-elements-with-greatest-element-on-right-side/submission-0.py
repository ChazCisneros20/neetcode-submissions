class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            max = 0
            for j in range(i+1, n):
                if arr[j] > max:
                    max = arr[j]
            arr[i] = max
        arr[n-1] = -1
        return arr