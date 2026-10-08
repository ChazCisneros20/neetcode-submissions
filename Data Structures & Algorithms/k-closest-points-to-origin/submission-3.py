class Solution:
    #=====QUICKSORT SOLUTION : OLDDDDD=====
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     if len(points) == 0:
    #         return [] 
    #     def quickSort(arr, s, e):
    #         if e-s+1<=1:
    #             return arr
    #         left = s
    #         pivot = arr[e]
    #         pivotDistance = ((arr[e][0]-0)**2 + (arr[e][1]-0)**2)**0.5
            
    #         #//Partition:
    #         for i in range(s, e):
    #             arrDistance = ((arr[i][0]-0)**2 + (arr[i][1]-0)**2)**0.5
    #             if arrDistance < pivotDistance:
    #                 #//SWAP arr[left] and arr[i]
    #                 arr[left], arr[i] = arr[i], arr[left]
    #                 left+=1
    #             #i+=1
            
    #         #//Finally: Swap the pivot with left
    #         arr[left],arr[e] = arr[e],arr[left]

    #         #//QuickSort left side subarray
    #         quickSort(arr, s, left-1)
    #         #//QuickSort right side subarray
    #         quickSort(arr, left+1, e)

    #         return arr 

    #     distances = quickSort(points, 0, len(points)-1)
    #     return distances[:k]
    class MinDistanceHeap:
        def __init__(self):
            self.heap = [0]
        def push(self, value):
            if len(self.heap)==1:
                self.heap.append(value)
            i = len(self.heap)-1
            while i//2 > 0:
                # percolate up. 
                if (self.heap[i][0]**2+self.heap[i][1]**2) > (self.heap[i//2][0]**2+self.heap[i//2][1]**2):
                    # if im bigger than my parent.
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i//2]
                    self.heap[i//2] = tmp 
                    i=i//2
        def pop(self):
            if len(self.heap)==1:
                return None 
            if len(self.heap)==2:
                return self.heap.pop() 
            i = 1 
            popped_result = self.heap[1]
            self.heap[1]=self.heap.pop() 
            while i*2 < len(self.heap):
                if (i*2+1 < len(self.heap) and (self.heap[i][0]**2+self.heap[i][1]**2) > (self.heap[i*2+1][0]**2+self.heap[i*2+1][1]**2) and (self.heap[i*2+1][0]**2+self.heap[i*2+1][1]**2) < (self.heap[i*2][0]**2+self.heap[i*2][1]**2)):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = tmp 
                    i=i*2+1
                elif (self.heap[i][0]**2+self.heap[i][1]**2) > (self.heap[i*2][0]**2+self.heap[i*2][1]**2):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2]
                    self.heap[i*2] = tmp 
                    i=i*2
                else:
                    break 
            return popped_result 
        def heapify(self, arr):
            self.heap = arr.copy()
            self.heap.append(self.heap[0])
            self.heap[0] = 0
            curr = (len(self.heap)-1)//2
            while curr > 0:
                i = curr 
                # check downard. percolate downard.
                while i*2 < len(self.heap):
                    if (i*2+1 < len(self.heap) and (self.heap[i][0]**2+self.heap[i][1]**2) > (self.heap[i*2+1][0]**2+self.heap[i*2+1][1]**2) and (self.heap[i*2+1][0]**2+self.heap[i*2+1][1]**2) < (self.heap[i*2][0]**2+self.heap[i*2][1]**2)):
                        tmp = self.heap[i]
                        self.heap[i] = self.heap[i*2+1]
                        self.heap[i*2+1] = tmp 
                        i=i*2+1
                    elif (self.heap[i][0]**2+self.heap[i][1]**2) > (self.heap[i*2][0]**2+self.heap[i*2][1]**2):
                        tmp = self.heap[i]
                        self.heap[i] = self.heap[i*2]
                        self.heap[i*2] = tmp 
                        i=i*2
                    else:
                        break 
                curr-=1
        def top(self):
            if len(self.heap)<=1:
                return None 
            return self.heap[1]

            

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #FIXME: Build a custom heap but does internal node swapping based on a^2 + b^2 values.
        pointsHeap = self.MinDistanceHeap()
        pointsHeap.heapify(points)
        res=[]
        for i in range(k):
            res.append(pointsHeap.pop())
        return res 

     
