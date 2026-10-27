class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None 
        self.prev = None 
class Pair:
    def __init__(self, key, value):
        self.key = key 
        self.val = value

class LRUCache:
    #HASHMAP for get/put. but LINKEDLIST for LRU/MRU 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {} 
        self.size = 0 
        self.headLRU = None
        self.tailMRU = None

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1   
        else: #assumes 1+ nodes if key IS IN self.hashMap
            #we need to find if the k:v that is .get()'d is 
            # a node in the headLRU, inbetween two nodes, or tailLRU. 
            value = self.hashMap[key]
            pair = Pair(key, value)
            node = ListNode(pair)
            curr = self.headLRU 
            while curr and curr.next:
                if curr.val.key == key:
                    break 
                curr = curr.next 
            if self.headLRU == self.tailMRU and curr==self.headLRU:
                return value 
            elif curr==self.headLRU:   #if the node to update is the headLRU
                self.headLRU = self.headLRU.next 
                self.headLRU.prev = None 
                #"append" new tail 
                self.tailMRU.next = node 
                node.prev = self.tailMRU
                self.tailMRU = node 
                return value
            elif curr==self.tailMRU: #if we want the tailMRU, just return value, do nothing.
                return value 
            else:                    #if the node to update is inbetween two nodes. 
                #delete
                curr.prev.next = curr.next  
                curr.next.prev = curr.prev 
                curr.prev = None 
                curr.next = None 
                #"append" new tail 
                self.tailMRU.next = node 
                node.prev = self.tailMRU
                self.tailMRU = node  
                return value 

    def put(self, key: int, value: int) -> None:
        pair = Pair(key, value)
        node = ListNode(pair)
        #This works for 1-to-self.capacity nodes b/c updating the value
        #does not add/delete anything, only swapping listnode placements 
        if key in self.hashMap: #if succeeds, 1+ nodes could exist.
            self.hashMap[key] = value 
            if self.headLRU==self.tailMRU: #1 NODE
                self.headLRU.val.val = value 
            else:                          #2+ NODES
                curr = self.headLRU
                while curr and curr.next:
                    if curr.val.key == key: #ensured this works, because it checks if its in hashmap
                        break 
                    curr=curr.next
                if curr==self.headLRU:   #if the node to update is the headLRU
                    self.headLRU = self.headLRU.next 
                    #"append" new tail 
                    self.tailMRU.next = node 
                    node.prev = self.tailMRU
                    self.tailMRU = node 
                elif curr==self.tailMRU: #if the node to update is the tailMRU. update k:v pair val
                    self.tailMRU.val.val = value 
                else:                    #if the node to update is inbetween two nodes. 
                    #delete
                    curr.prev.next = curr.next  
                    curr.next.prev = curr.prev 
                    curr.prev = None 
                    curr.next = None 
                    #"append" new tail 
                    self.tailMRU.next = node 
                    node.prev = self.tailMRU
                    self.tailMRU = node  
        elif self.size < self.capacity:
            #key does not exist and the size<capacity[BUILD THE LIST; ADD TO HASHMAP]
            self.hashMap[key] = value
            self.size+=1
            if not self.headLRU: #0 NODES
                self.headLRU = node
                self.tailMRU = node 
            else:                #1+ NODES
                self.tailMRU.next = node 
                node.prev = self.tailMRU
                self.tailMRU = node     
        else: #self.size==self.capacity:
            self.hashMap[key] = value
            if self.headLRU == self.tailMRU: #if self.size==self.capacity AND self.capacity=1
                del self.hashMap[self.headLRU.val.key]
                self.headLRU = node
                self.tailMRU = node 
            else: #2+ node capacity
                del self.hashMap[self.headLRU.val.key]
                self.headLRU = self.headLRU.next 
                self.headLRU.prev = None 
                self.tailMRU.next = node 
                node.prev = self.tailMRU 
                self.tailMRU = node 





            





        


