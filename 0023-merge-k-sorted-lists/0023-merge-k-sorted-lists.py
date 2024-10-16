# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummylist3 = ListNode(-1)
        def mergeTwoLists(list1, list2, list3):
            while list1 != None or list2 != None:
                if list1 != None and list2 != None:
                    if list1.val > list2.val:
                        Node = ListNode(list2.val)
                        list2 = list2.next
                    else:
                        Node = ListNode(list1.val)
                        list1 = list1.next 
                elif list2 != None and list1 == None:
                    Node = ListNode(list2.val)
                    list2 = list2.next
                else:
                    Node = ListNode(list1.val)
                    list1 = list1.next
                list3.next = Node
                list3 = list3.next
            lists.append(dummylist3.next)
            return list3
            
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            if list1 != None or list2 != None:
                mergeTwoLists(list1, list2, dummylist3) 
        return dummylist3.next
                
           
            
            
            
        