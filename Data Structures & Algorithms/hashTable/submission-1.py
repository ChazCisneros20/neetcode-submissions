class Pair:
    def __init__(self, key, value):
        self.key = key 
        self.val = value
class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = []
        for i in range(capacity):
            self.map.append(None)
    def hash(self, key):
        sumASCII = 0
        for c in str(key):
            sumASCII+=ord(c)
        return sumASCII % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        # HashMap implementation ensures always 50%+ vacancy indexes.
        # Loop indefinitley until vacancy found (logic ensures this)
        while True:
            if self.map[index] == None:    #<- it is found
                self.map[index] = Pair(key, value)
                self.size+=1
                if self.size >= self.capacity//2:
                    self.resize()   #<- or rehash(), depends on implementation
                return 
            elif self.map[index].key == key:   #<- key already exists; overwrite value
                self.map[index].val = value 
                return 
            # open address increment until it is found
            index+=1 
            index = index%self.capacity 

    def get(self, key: int) -> int:
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val 
            #open address increment until it is found
            index+=1
            index=index%self.capacity 
        return -1 


    def remove(self, key: int) -> bool:
        
        if self.get(key) == -1: #<- use .get() method to see if it is in HashMap 
            return False 
        index = self.hash(key)
        # it is in HashMap (logic ensures this) 
        while self.map[index] != None:
            #similar logic to .put() 
            if self.map[index].key == key: 
                self.map[index].key = "TOMBSTONE" 
                self.size-=1
                return True
            # open address increment until its found  
            index+=1 
            index=index%self.capacity 

    def getSize(self) -> int:
        return self.size 

    def getCapacity(self) -> int:
        return self.capacity 

    def resize(self) -> None:
        self.capacity*=2
        oldMap = self.map 
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        self.map = newMap 
        self.size = 0 
        for pair in oldMap:
            if pair is not None and pair.key != "TOMBSTONE":
                # will update .size 
                self.insert(pair.key, pair.val) 

