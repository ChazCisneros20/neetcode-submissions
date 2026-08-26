# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def qs(self, arr, s, e):
        #//If the difference of e and s is <= 1 then the subarray passed is one-element
        if e-s+1<=1:
            return arr
        left = s 
        pivot = arr[e].key
        #//Partition Loop:
        for i in range(s, e):
            #//This works if the pivot chosen was the start, middle, random. Same logic applies. 
            #//Smaller values before pivot, bigger after pivot
            if arr[i].key < pivot:
                #//Swap arr[left] <--> arr[i]
                arr[left], arr[i] = arr[i], arr[left]
                left+=1
            #i+=1
        
        #//Always end with swapping left with pivot incase left is on a value larger than pivot
        arr[left], arr[e] = arr[e], arr[left]

        #//Quicksort left-hand side
        self.qs(arr, s, left-1) #//Left-1 b/c left itself is in sorted place.
        #//Quicksort right-hand side
        self.qs(arr, left+1, e) #//Left+1 b/c left iself is in sorted place

        #return arr AFTER all sub-problems, subarrays are sorted in place. 
        return arr

                    

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs)==0:
            return []
        return self.qs(pairs, 0, len(pairs)-1)
        #We will use end pivot method
        