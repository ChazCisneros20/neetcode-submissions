class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        #NEW for CHAINING: .next-> pointer
        self.next = None
class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0 
        self.map = [None] * capacity 
    def hash_function(self, key):
        #our keys are only natural numbers, so no ascii summation
        return key % self.capacity
    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        head = self.map[index]
        if not head:           # if no head, just create it.
            self.map[index] = Pair(key, value)
        else:                  # if head exists...
            # traverse until you find the key (to overwrite), at the end, just append as new node
            prev = None
            while head:                     # <-
                if head.key == key:
                    head.val = value 
                    return 
                prev,head = head, head.next # <- THIS WILL ALWAYS RUN ONCE. [prev]->[head=None]
            #b/c the logic ensures prev is always the tail and head is a [None] value
            prev.next = Pair(key,value)
        self.size+=1
        if self.size >= self.capacity//2:
            self.resize() 
    def get(self, key: int) -> int:
        index = self.hash_function(key)

        head = self.map[index]
        while head:
            if head.key == key:
                return head.val 
            head = head.next 
        #if head traverses all the way and never returns head.val, 
        # return -1 as it exits the loop. OR if head never existed (vacant spot). also return -1
        return -1 
    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.map[index]
        prev = None
        
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next 
                    self.size-=1
                    return True
                else: #<- for rare case where the head is the one to remove, prev is [None]
                    self.map[index] = head.next # we move head up ONE node
                    self.size-=1
                    return True              
            prev,head=head,head.next
        #if we've exhuasted head=head.next traversal and reached end of list ([None])
        # it means we couldn't find it in that key's chain
        return False 
    def getSize(self) -> int:
        return self.size
    def getCapacity(self) -> int:
        return self.capacity
    def resize(self) -> None:
        self.capacity*=2
        self.size = 0 
        newMap = [None] * self.capacity
        #traverse each element in old map
        #if a node exists, continue down that chain, adding to the newMap
        for node in self.map:
            while node:
                index = self.hash_function(node.key) #using our new self.capacity -> NEW index placement
                if newMap[index]:
                    node.next = newMap[index] # [node]->[head]->....
                    newMap[index] = node
                    self.size+=1  
                else: # if there is no head node, just simply place it in. 
                    newMap[index] = node
                    self.size+=1  
                node = node.next 
        self.map = newMap #bye bye old map!




