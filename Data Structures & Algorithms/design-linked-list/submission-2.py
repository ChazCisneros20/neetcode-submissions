class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
    def get(self, index: int) -> int:
        #if 0
        if not self.head:
            return -1
        #if 1
        elif self.head==self.tail:
            if index > 0 or index < 0:
                return -1
            else:
                return self.head.val
        #if 2+
        else:
            i = 0 
            curr = self.head
            while i < index and curr:
                curr = curr.next
                i+=1
            if curr:
                return curr.val
            else:
                return -1 
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:    
            node.next = self.head 
            self.head.prev = node
            self.head = node 
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node 
            node.prev = self.tail 
            self.tail = node 
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        node = ListNode(val)
        if not self.head:
            if index > 0:
                return
            else:
                self.head = node
                self.tail = node
        else:
            if index==0:
                self.addAtHead(val)
            else:
                i = 0
                prev = None
                curr = self.head
                #Keep loop till curr lands on index. 
                while i < index and curr:
                    prev = curr 
                    curr = curr.next
                    i+=1
                #Less edge-cases bc of double links
                if i==index:
                    #If the index is within the list,
                    if curr:
                        prev.next = node
                        node.prev = prev 
                        node.next = curr
                        curr.prev = node 
                    else: #If the index landed on one past the tail. (Append to the tail!)
                        prev.next = node 
                        node.prev = prev 
                        self.tail = node 
                else:
                    return 
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return 
        if not self.head:
            return
        elif self.head==self.tail:
            if index > 0:
                return
            else:
                self.head = None
                self.tail = None
        else:
            if index == 0:
                self.head.next.prev = None
                self.head.next = None 
            i = 0
            curr = self.head
            prev = None
            while i < index and curr:
                prev = curr
                curr = curr.next
                i+=1
            if i == index:
                if curr and curr.next: #We land on curr ...->[prev]->[curr]->[curr.next]->...
                    prev.next = curr.next 
                    curr.next.prev = prev
                    curr.next = None 
                    curr.prev = None
                elif curr: #We land on curr, no curr.next ...->[prev]->[curr]->None...
                    prev.next = curr.next 
                    curr.prev = None
                    self.tail = prev 
                #we land on the None right after the tail; [self.tail] -> [None]    
                else:
                    return 
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)