# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=None
        while list1 or list2 is not None:
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    if head == None:
                        list3 = ListNode(list1.val) 
                        head = list3
                    else:
                        list3.next = ListNode(list1.val)  
                        list3 = list3.next
                    list1 = list1.next
                else:
                    if head == None:
                        list3 = ListNode(list2.val) 
                        head = list3
                    else:
                        list3.next = ListNode(list2.val)  
                        list3 = list3.next
                    list2 = list2.next
            elif list1 == None:
                if head == None:
                    list3 = ListNode(list2.val) 
                    head = list3
                else:
                    list3.next = ListNode(list2.val)  
                    list3 = list3.next
                list2 = list2.next
            else:
                if head == None:
                    list3 = ListNode(list1.val) 
                    head = list3
                else:
                    list3.next = ListNode(list1.val)  
                    list3 = list3.next
                list1 = list1.next
        return head
            
            