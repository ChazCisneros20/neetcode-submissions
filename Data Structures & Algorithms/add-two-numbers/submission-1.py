# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def concatNumber(l1):
            if not l1:
                return 0
            else:
                n1 = concatNumber(l1.next)
                n1 = (n1 * 10) + l1.val 
                return n1 
        n1 = concatNumber(l1)
        n2 = concatNumber(l2)
        val = str(n1+n2)[::-1]
        n = len(val)
        node = ListNode()
        head = node 
        for i in range(n):
            if i == n-1:
                node.val = val[i]
            else:
                node.val = val[i]
                temp = ListNode()
                node.next = temp 
                node = temp 
        
        return head
        
        

