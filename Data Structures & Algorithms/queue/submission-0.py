class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None 
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        else: 
            return False

    def append(self, value: int) -> None:
        node = ListNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            #...->[self.tail]->[node]->None...
            self.tail.next = node 
            node.prev = self.tail 
            self.tail = node 

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            node.next = self.head 
            self.head.prev = node
            self.head = node 

    def pop(self) -> int:
        if not self.head:
            return -1
        elif self.head==self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None 
            return value
        else:
            value = self.tail.value

            self.tail = self.tail.prev 
            self.tail.next.prev = None
            self.tail.next = None 
            return value

        

    def popleft(self) -> int:
        if not self.head:
            return -1
        elif self.head==self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.value
            self.head = self.head.next 
            self.head.prev.next = None
            self.head.prev = None 
            return value
        
