class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:
        if (len(self.minStack) == 0):
            self.minStack.append(val);
        #It MUST be val <= minStack[-1]. Duplicate minimums are required for the data structure to work. 
        elif (len(self.minStack) > 0 and val <= self.minStack[-1]):
        
            self.minStack.append(val);
        
        self.stack.append(val);
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.minStack[-1]:
                del self.minStack[-1]
            #No matter what, we still delete stack[n-1]
            del self.stack[-1]
        
        
        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        
