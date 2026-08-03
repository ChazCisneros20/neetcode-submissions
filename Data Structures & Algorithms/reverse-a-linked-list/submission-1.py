# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        prev = None
        curr = head 
        #1) prev=None, curr=head. [0]->None. prev=[0] curr=[1]. 2) [1]->[0]->None prev=[1], curr=[2]. 3) [2]->[1]->[0]->None
        while curr is not None:
            curr_next = curr.next 
            #make node point back
            curr.next = prev
            #make the prev var iterate up
            prev = curr
            #curr var iterates up 
            curr = curr_next
        return prev 
