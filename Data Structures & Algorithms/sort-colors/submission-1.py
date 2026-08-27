class ListNode:
    def __init__(self, val=0):
        self.value = val
        self.next = None
        self.prev = None 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #// Dummy's for each 0,1,2 value. 
        zeroDummy = ListNode()
        twoDummy  = ListNode()
        threeDummy= ListNode()
        bucket = [zeroDummy, twoDummy, threeDummy]

       
        for n in nums:
            #// if a bucket value has only its dummy node.
            if not bucket[n].next:
                bucket[n].next = ListNode(n)
            else:
                node = ListNode(n)
                node.next = bucket[n].next
                node.prev = bucket[n] 
                bucket[n].next.prev = node
                bucket[n].next = node 
        i=0
        #// 0 to 2 inclusive 
        for n in range(0, len(bucket)):
            #// Start at .next b/c each bucket index has a dummyHead
            curr = bucket[n].next
            while curr:
                nums[i] = (curr.value)
                curr = curr.next
                i+=1  
            
                

            
        

