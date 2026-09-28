# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(start, middle, end, pairs):
            arr1 = pairs[start:middle+1]
            arr2 = pairs[middle+1:end+1]
            i=0
            j=0
            k=start
            while i < len(arr1) and j < len(arr2):
                if arr1[i].key <= arr2[j].key:
                    pairs[k] = arr1[i]
                    i+=1
                else:
                    pairs[k] = arr2[j]
                    j+=1
                k+=1
            while i < len(arr1):
                pairs[k] = arr1[i]
                i+=1
                k+=1
            while j < len(arr2):
                pairs[k] = arr2[j]
                j+=1
                k+=1
            
                


        def ms(start, end, pairs):
            if (end-start+1) <= 1: #// if there is one element left
                return pairs
            
            mid = (start+end)//2

            #// mergeSort left-half
            ms(start, mid, pairs)
            #// mergeSort right-half
            ms(mid+1, end, pairs)
            #// merge the two single elements and go up call stack 
            merge(start, mid, end, pairs)
            #// to merge two subarrays of two elements each or two subarrays of two elements and one of one element
            return pairs
        return ms(0, len(pairs)-1, pairs)
