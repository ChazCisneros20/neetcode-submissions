class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = ListNode(x)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node 


    def pop(self) -> int:
        if not self.head:
            return 
        elif self.head==self.tail:
            value = self.tail.value
            self.head=None
            self.tail=None
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None 
            return value 

    def top(self) -> int:
        if not self.head:
            return 
        else:
            return self.tail.value 

    def empty(self) -> bool:
        if not self.head:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()