class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n > 1:
            for i in range(n-2, -1, -1):
                if i == n-2:
                    val = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = -1
                else:
                    elem = arr[i]
                    arr[i] = max(val, arr[i+1])
                    val = elem
            return arr

        else:
            arr[0] = -1
            return arr