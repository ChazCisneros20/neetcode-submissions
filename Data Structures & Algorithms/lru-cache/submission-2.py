class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        #initialize a hashamp. it holds key:node. the node has same key as the key. 
        self.hashCache = {} 
        #initialize a linked list
        self.left = ListNode(0,0)  #LEFTMOST DUMMY
        self.right = ListNode(0,0) #RIGHTMOST DUMMY
        self.left.next = self.right 
        self.right.prev = self.left 
        

    def get(self, key: int) -> int:
        if key not in self.hashCache:
            return -1 
        #use the hashMap as an O(1) retrieval of the node to use at all time
        self.delete_node(self.hashCache[key])
        self.insert_at_MRU(self.hashCache[key])
        return self.hashCache[key].val
         

    def put(self, key: int, value: int) -> None:
        if key in self.hashCache:
            #delete node if it exists
            self.delete_node(self.hashCache[key])
        node = ListNode(key, value)
        self.hashCache[key] = node 
        self.insert_at_MRU(node)
        # if we are at capacity, evict the LRU (leftmost node)
        if len(self.hashCache) > self.capacity:
            LRU = self.left.next
            self.delete_node(LRU)
            del self.hashCache[LRU.key]
    def insert_at_MRU(self, node):
        node.prev = self.right.prev 
        node.next = self.right 
        self.right.prev.next = node 
        self.right.prev = node 
    def delete_node(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev 
        node.prev, node.next = None, None 
        
