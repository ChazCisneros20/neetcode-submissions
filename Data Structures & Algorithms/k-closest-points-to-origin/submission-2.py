class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0:
            return [] 
        def quickSort(arr, s, e):
            if e-s+1<=1:
                return arr
            left = s
            pivot = arr[e]
            pivotDistance = ((arr[e][0]-0)**2 + (arr[e][1]-0)**2)**0.5
            
            #//Partition:
            for i in range(s, e):
                arrDistance = ((arr[i][0]-0)**2 + (arr[i][1]-0)**2)**0.5
                if arrDistance < pivotDistance:
                    #//SWAP arr[left] and arr[i]
                    arr[left], arr[i] = arr[i], arr[left]
                    left+=1
                #i+=1
            
            #//Finally: Swap the pivot with left
            arr[left],arr[e] = arr[e],arr[left]

            #//QuickSort left side subarray
            quickSort(arr, s, left-1)
            #//QuickSort right side subarray
            quickSort(arr, left+1, e)

            return arr 

        distances = quickSort(points, 0, len(points)-1)
        return distances[:k]