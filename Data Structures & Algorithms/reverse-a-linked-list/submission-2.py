# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Will stop when ...->[tail]->None... ON 
        #Will stop when ...->[3]->None... ON
        #where head will be ...[tail]...
        #where head will be ...[3]... 
        if not head or not head.next:
            return head
        else:
            #It should recursively stack depth until it hits the base case
            #giving us our finalized newHead outcome.
            newHead = self.reverseList(head.next)
            head.next.next = head 
            head.next = None
        
        return newHead 
            
            

        

