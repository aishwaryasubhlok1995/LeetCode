# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head
        if head == None:
            return 
        while curr != None:
            if curr.val in temp:
                prevNode.next = curr.next
            else:
                temp.append(curr.val)
                prevNode = curr
            curr= curr.next
        return head
            
        