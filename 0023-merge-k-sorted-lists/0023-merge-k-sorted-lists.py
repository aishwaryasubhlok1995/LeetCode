# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            currentMergeList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                currentMergeList.append(self.mergeTwoLists(list1, list2)) 
            lists = currentMergeList
        return lists[0]
    
    def mergeTwoLists(self, list1, list2):
        dummylist3 = ListNode(-1)
        current = dummylist3
        while list1 or list2:
            if list1 == None:
                current.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 == None:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    current.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    current.next = ListNode(list1.val)
                    list1 = list1.next 
            current =  current.next
        return dummylist3.next 
                
           
            
            
            
        