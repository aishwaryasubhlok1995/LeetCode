# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        list3 = ListNode(-1)
        head = list3
        if list1 == None and list2 == None:
            return None
        while list1 != None or list2 != None:
            if list1 == None:
                node = ListNode(list2.val)
                list2 = list2.next 
            elif list2 == None:
                node = ListNode(list1.val)
                list1 = list1.next
            elif (list1.val > list2.val):
                node = ListNode(list2.val)
                list2 = list2.next 
            else: 
                node = ListNode(list1.val)
                list1 = list1.next
            list3.next = node
            list3 = list3.next
        return head.next
            
        
                
                
                