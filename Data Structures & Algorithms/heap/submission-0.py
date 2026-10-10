class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        if len(self.heap)==1:
            self.heap.append(val)
            return
        self.heap.append(val)
        i = len(self.heap)-1
        while i//2 > 0 and self.heap[i//2] > self.heap[i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp 
            i=i//2

    def pop(self) -> int:
        if len(self.heap)==1:
            return -1
        if len(self.heap)==2:
            return self.heap.pop() 
        popped_result = self.heap[1]
        self.heap[1] = self.heap.pop() 
        i = 1
        while i*2 < len(self.heap):
            if i*2+1 < len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[i*2+1] < self.heap[i*2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2+1]
                self.heap[i*2+1] = tmp 
                i = i*2+1
            elif self.heap[i] > self.heap[i*2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = tmp 
                i = i*2
            else: 
                break
        return popped_result

    def top(self) -> int:
        if len(self.heap) <= 1: 
            return -1 
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums.copy()
        curr = (len(self.heap)-1)//2
        while curr > 0:
            i = curr
            while i*2 < len(self.heap):
                if i*2+1 < len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[i*2+1] < self.heap[i*2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2+1]
                    self.heap[i*2+1] = tmp 
                    i = i*2+1
                elif self.heap[i] > self.heap[i*2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i*2]
                    self.heap[i*2] = tmp 
                    i = i*2
                else: 
                    break
            curr-=1
        
        
        