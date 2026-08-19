# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #If one is literally just None, we still need to iterate 
        if not list1:
            return list2
        elif not list2:
            return list1

        prev = None
        head = None
        if list2.val <= list1.val:
            head = list2
            prev = list2
            list2 = list2.next 
        else:
            head = list1
            prev = list1
            list1 = list1.next 
        while list1 or list2:
            if list2 and list1:
                if list2.val <= list1.val:
                    prev.next = list2
                    prev = list2
                    list2=list2.next
                else:
                    prev.next = list1
                    prev = list1
                    list1=list1.next
            #If a list becomes empty. Just try to iterate the remaining one until while condition breaks out. 
            else:    
                if list1 and not list2:
                    prev.next = list1
                    prev = list1
                    list1 = list1.next 
                #if list2 and not list1:
                else:
                    prev.next = list2
                    prev = list2
                    list2 = list2.next
        return head
                
                
            
            #curr=curr.next for both lists. 
            
    
        