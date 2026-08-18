# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0:
            return []

        def merge(arr, s, m, e):
            arr1 = arr[s:m+1]
            arr2 = arr[m+1:e+1]
            i=0
            j=0
            k=s
            
            while (i<len(arr1) and j<len(arr2)):
                #Must be <= with equality(=) to ensure STABLE
                if arr1[i].key <= arr2[j].key:
                    arr[k] = arr1[i]
                    i+=1
                    k+=1
                else:# arr2[j] < arr1[i]
                    arr[k] = arr2[j]
                    j+=1
                    k+=1
            while i<len(arr1):
                arr[k] = arr1[i]
                i+=1
                k+=1
            while j<len(arr2):
                arr[k] = arr2[j]
                j+=1
                k+=1
            
        def ms(arr, s, e):
            if (e-s)+1 <= 1:
                return arr
            else:
                m = (s+e)//2
                #mergeSort the lefthalf-subarray
                ms(arr, s, m)
                #mergeSort the righthalf-subarray
                ms(arr, m+1, e)
                #merge the two pre-sorted subarrays using k-merge algorithm
                merge(arr, s, m, e)
        ms(pairs, 0, len(pairs)-1)
        return pairs 