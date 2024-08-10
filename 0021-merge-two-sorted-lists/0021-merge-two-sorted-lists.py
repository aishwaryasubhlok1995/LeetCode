# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        list3 = None
        if list1 == None and list2 == None:
            return list3
        def createNode(val, list3):
            if list3 == None:
                head = ListNode(val, None)
            else:
                head = list3
                curr = head
                while curr.next != None:
                    curr = curr.next 
                curr.next = ListNode(val, None)
            return head
        while list1 != None or list2 != None:
            if list1 == None:
                list3 = createNode(list2.val, list3)
                list2 = list2.next 
            elif list2 == None:
                list3 = createNode(list1.val, list3)
                list1 = list1.next
            elif (list1.val > list2.val):
                list3 = createNode(list2.val, list3)
                list2 = list2.next 
            else: 
                list3 = createNode(list1.val, list3)
                list1 = list1.next
        return list3
            
        
                
                
                