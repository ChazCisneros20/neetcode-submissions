class ListNode:
    def __init__(self, url):
        self.next = None
        self.prev = None
        self.value = url 

class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head = node
        self.tail = node 
        self.location = node 
        

    def visit(self, url: str) -> None:
        node = ListNode(url)
        if not self.head:
            self.head = node
            self.tail = node 
            self.location = node
        else:
            self.location.next = node 
            node.prev = self.location 
            node.next = None
            self.location = node 
            self.tail = node 
            #node is default ...<-[self.location]-><-[node]->None...
            # now is         ...<-[nodeX]-><-[self.location]->None...
    def back(self, steps: int) -> str:
        #traverse back, but don't change pointers. Leave list as is.
        n = steps
        if not self.head:
            return
        elif self.head == self.tail:
            return self.head.value
        else:
            #iterate n times
            i = 0 
            while i < n and self.location.prev:
                self.location = self.location.prev 
                i+=1
            return self.location.value 
            
        

    def forward(self, steps: int) -> str:
        n = steps
        if not self.head:
            return
        else:
            i = 0
            while i < n and self.location.next:
                self.location = self.location.next
                i+=1
            return self.location.value  
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)