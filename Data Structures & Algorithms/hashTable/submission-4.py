class Pair:
    def __init__(self, key, value):
        self.key = key 
        self.val = value
class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.map = [None] * capacity
        self.size = 0 
    def hash(self, key):
        ascii_sum = 0 
        for c in str(key):
            ascii_sum+=ord(c)
        index = ascii_sum % self.capacity
        return index
    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True: 
            if self.map[index] == None: # if vacant spot
                self.map[index] = Pair(key, value)
                self.size+=1
                #// if size is over half capacity 
                if self.size >= self.capacity//2:
                    self.resize()
                return
            elif self.map[index].key == "TOMBSTONE":
                self.map[index] = Pair(key, value)
                self.size+=1 
                if self.size >= self.capacity//2:
                    self.resize()
                return 
            elif self.map[index].key == key: # if key exists; overwrite val
                self.map[index].val = value
                return 
            index+=1 # open address incrementing
            index = index%self.capacity 
    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None: # open-address increment `index` til key is found. stop if [None]
            if self.map[index].key == key:
                return self.map[index].val
            index+=1
            index = index%self.capacity
        return -1 

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False 
        index = self.hash(key)
        while True:
            if self.map[index] is not None and self.map[index].key == key:
                self.map[index].key = "TOMBSTONE" 
                self.size-=1
                return True 
            index+=1 
            index = index%self.capacity

    def getSize(self) -> int:
        return self.size 

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        #resize AND rehash
        self.capacity*=2 
        oldMap = self.map
        newMap = [] 
        for i in range(self.capacity):
            newMap.append(None)
        self.map = newMap 
        self.size=0
        for element in oldMap:
            if element is not None and element.key != "TOMBSTONE":
                self.insert(element.key, element.val)
    def print(self):
        for element in self.map:
            if element is not None and element.key != "TOMBSTONE":
                print(element.key, element.val, end=" ")
        
                

