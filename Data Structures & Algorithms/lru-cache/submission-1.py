class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hashMap = {} 
        self.left = ListNode(0,0) #DUMMY before HEADLRU
        self.right = ListNode(0,0) #DUMMY after TAILMRU
        self.left.next = self.right
        self.right.prev = self.left 
        # dummies let us delete, move, all without worrying about edge cases 

    def deleteNode(self, node):
        #THIS CAN DELETE ANY NODE, IF ITS 1ST NODE, INBETWEEN, OR LAST NODE DUE TO DUMMIES.
        node.prev.next = node.next
        node.next.prev = node.prev 
    def insert_at_front(self, node):
        self.right.prev.next = node   #[]->[node]    [right]
        node.prev = self.right.prev   #[]-><-[node]
        node.next = self.right        #[]-><-[node]->[right]
        self.right.prev = node        #[]-><-[node]<-->[right]
    def get(self, key: int) -> int:
        #should insert_at_front 
        if key in self.hashMap:
            self.deleteNode(self.hashMap[key])
            self.insert_at_front(self.hashMap[key])
            return self.hashMap[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        #if exists in cache, delete node and insert new node with same key, updated value 
        #simply build/chain linked list if < capacity 
        # else, shift headLRU (delete old head)
        if key in self.hashMap:
            self.deleteNode(self.hashMap[key])
        self.hashMap[key] = ListNode(key, value) #either add k:v or overwrite v
        self.insert_at_front(self.hashMap[key])  #access node 0(1) using hashmap
        # if we are beyond capacity, delete leftmost node from linkedlist and hashmap
        if len(self.hashMap) > self.capacity:
            LRU = self.left.next
            self.deleteNode(self.left.next)
            del self.hashMap[LRU.key] #we pass in the headLRU and let the function handle it
             

        
