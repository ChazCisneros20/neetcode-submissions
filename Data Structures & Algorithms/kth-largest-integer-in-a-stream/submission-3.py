class minHeap:
    def __init__(self):
        self.heap = [0] 
    def push(self, value):
        if len(self.heap)==1:
            self.heap.append(value)
            return 
        self.heap.append(value)
        i = len(self.heap)-1
        #percolate up. 
        while i//2 > 0:
            if self.heap[i//2] > self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = tmp 
            i=i//2
    def pop(self):
        if len(self.heap)==1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        popped_result = self.heap[1]
        self.heap[1] = self.heap.pop() 
        #percolate down. 
        i = 1
        while i*2 < len(self.heap):
            if (i*2+1 <len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[i*2+1] < self.heap[i*2]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2+1]
                self.heap[i*2+1] = tmp 
                i=i*2+1
            elif self.heap[i] > self.heap[i*2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = tmp 
                i=i*2
            else:
                break 

        return popped_result
    def heapify(self, arr):
        if len(arr) == 0:
            return None 
        self.heap = [0] + arr.copy()
        # start from halfway of node array, scan leftward (up tree right-to-left from bottom up)
        # percolate down if needed. 
        curr = (len(self.heap)-1)//2
        while curr > 0:
            i = curr
            while i*2 < len(self.heap):
                if (i*2+1 < len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[i*2+1] < self.heap[i*2]):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = tmp 
                    i=i*2+1
                elif self.heap[i] > self.heap[i*2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2]
                    self.heap[i*2] = tmp 
                    i=i*2
                else:
                    break 
            curr-=1
    def length(self):
        return len(self.heap)-1
    def view(self):
        if len(self.heap) < 0:
            return None 
        return self.heap[1]

        

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.MinHeap = minHeap()
        self.MinHeap.heapify(nums)
        while self.MinHeap.length() > k:
            self.MinHeap.pop() 
        
    def add(self, val: int) -> int:
        # if the heap is less than k values, push it but return None because there is no "kth" largest element
        if self.MinHeap.length() < self.k:
            self.MinHeap.push(val)
            return self.MinHeap.view()
    
        # if the new value is > heap then we need to remove the top, why? because it means that the top 
        # will become the k+1'th element, which is out of bounds, so let's remove the k+1'th element, 
        # put in the new k'th element, then return it using .view()
        if val > self.MinHeap.view():
            self.MinHeap.pop()
            self.MinHeap.push(val)
    
        return self.MinHeap.view()