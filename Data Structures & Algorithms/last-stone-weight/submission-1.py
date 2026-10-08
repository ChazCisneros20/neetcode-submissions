class MaxHeap:
    def __init__(self):
        self.heap = [0] 
    def push(self,value):
        if len(self.heap)==1:
            self.heap.append(value)
            return 
        self.heap.append(value)
        i = len(self.heap)-1
        while i//2 > 0 and self.heap[i//2] < self.heap[i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp 
            i = i//2 
    def pop(self):
        if len(self.heap)==1:
            return None
        if len(self.heap)==2:
            return self.heap.pop()  
        pop_res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i=1
        while i*2 < len(self.heap):
            if i*2+1 < len(self.heap) and self.heap[i] < self.heap[i*2+1] and self.heap[i*2+1] > self.heap[i*2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2+1]
                self.heap[i*2+1] = tmp
                i=i*2+1
            elif self.heap[i] < self.heap[i*2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = tmp
                i=i*2
            else:
                break 
        return pop_res 
    def heapify(self, arr):
        arr.append(arr[0])
        arr[0] = 0
        self.heap = arr 
        # half values dont have children, skip to (n-1)//2
        curr = (len(self.heap)-1)//2
        while curr > 0:
            i = curr
            #make sure its root and kids keep order property. percolate down 
            while i*2 < len(self.heap):
                if i*2+1 < len(self.heap) and self.heap[i] < self.heap[i*2+1] and self.heap[i*2+1] > self.heap[i*2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = tmp
                    i=i*2+1
                elif self.heap[i] < self.heap[i*2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2]
                    self.heap[i*2] = tmp
                    i=i*2
                else:
                    break 
            curr-=1 
    def length(self):
        return len(self.heap)-1 # do -1, if there's 4 array elements, it means there's 3 Heap nodes. 
    def top(self):
        if len(self.heap)==1:
            return None
        else:
            return self.heap[1]


        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        Heap = MaxHeap()
        Heap.heapify(stones)
        while Heap.length() > 1:
            y = Heap.pop() 
            x = Heap.pop() 
            if x<y:
                Heap.push(y-x)
        if Heap.top() is not None:
            return Heap.top() 
        else:
            return 0 

        