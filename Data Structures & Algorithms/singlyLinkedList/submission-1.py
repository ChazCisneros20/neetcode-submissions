class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        else:
            curr = self.head
            #So if index=2, then make index+1 =3 so it properly stops AT index 2.
            for i in range(index):
                if not curr:
                    return -1
                curr = curr.next 
            if curr:
                return curr.value
            else:
                return -1
            

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            node.next = self.head 
            self.head = node 
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        elif self.head==self.tail:
            if index > 0:
                return False
            else:
                self.head = None
                self.tail = None 
                return True
        else:
            if index == 0:
                self.head = self.head.next 
                return True
            else:
                prev = None
                curr = self.head
                for i in range(index):
                    if not curr:
                        return False
                    prev = curr 
                    curr = curr.next

                if curr and curr.next:
                    prev.next = curr.next
                    return True
                #Only curr, no curr.next ~= we land on tail. 
                elif curr: 
                    self.tail = prev
                    prev.next = None 
                    return True
        

    def getValues(self) -> List[int]:
        valueList = []
        curr = self.head
        while curr:
            valueList.append(curr.value)
            curr = curr.next
        return valueList
        
