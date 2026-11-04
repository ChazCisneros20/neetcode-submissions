class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val  
        self.next = None 
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        # map_cache stores : {key : Node(key, val)} for O(1) access of nodes in linkedlist
        #
        # no self.size, use len(map_cache) to track size
        #
        # [dummy_left]<-->[dummy_right]
        self.map_cache = {} 
        self.capacity = capacity 
        self.left_dummy = Node(0,0)
        self.right_dummy = Node(0,0)
        self.left_dummy.next = self.right_dummy
        self.right_dummy.prev = self.left_dummy
    def remove_from_list(self, key): 
        # only call if it is confirmed that this exists
        # deallocate from memory by seperating that node's pointers 
        # use that node's surrounding nodes (real nodes or dummies) to de-link it
        node = self.map_cache[key]
        node.prev.next, node.next.prev = node.next, node.prev 
        node.next = None 
        node.prev = None 
    def insert_at_MRU(self, node):
        # places this as the MRU 
        node.prev, node.next = self.right_dummy.prev, self.right_dummy 
        self.right_dummy.prev.next, self.right_dummy.prev = node, node 
    def get(self, key: int) -> int:
        if key not in self.map_cache:
            return -1 
        self.remove_from_list(key)
        self.insert_at_MRU(self.map_cache[key])
        return self.map_cache[key].val
    def put(self, key: int, value: int) -> None:
        if key in self.map_cache:
            self.remove_from_list(key)  
        node = Node(key, value)
        self.map_cache[key] = node  #will either add or overwrite k:v pair
        self.insert_at_MRU(node)
        #remove LRU leftmost node if > capacity 
        if len(self.map_cache) > self.capacity:
            LRU = self.left_dummy.next
            self.remove_from_list(LRU.key)
            del self.map_cache[LRU.key]

        
        
            
            
        
